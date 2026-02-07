"""Sensor platform for Systemair Modbus."""
from __future__ import annotations

import re

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN
from .entity import SystemairBaseEntity


# Prefixes we want to strip from internal keys to make nicer names/object_ids.
# Keep order from most specific to least specific.
_STRIP_PREFIXES: tuple[str, ...] = (
    "systemair_save_",
    "save_",
    "systemair_",
)


def _strip_prefixes(key: str) -> str:
    for p in _STRIP_PREFIXES:
        if key.startswith(p):
            return key[len(p) :]
    return key


def _pretty_name(key: str) -> str:
    """Convert internal key into a readable name."""
    key = _strip_prefixes(key)
    key = key.replace("_", " ").strip()
    # title-case but keep known acronyms
    name = " ".join(w.upper() if w in {"SAF", "EAF", "CO2"} else w.capitalize() for w in key.split())
    # Fix common words
    name = re.sub(r"\bTemp\b", "Temperature", name)
    return name


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    model = data["model"]

    entities: list[SensorEntity] = []

    # Register sensors (raw Modbus registers)
    for reg in model.REGISTER_MAP:
        if reg.platform != "sensor":
            continue
        entities.append(SystemairRegisterSensor(entry, coordinator, reg))

    # Derived sensors (computed values)
    for key, meta in model.DERIVED_MAP.items():
        if meta.get("platform") != "sensor":
            continue
        entities.append(SystemairDerivedSensor(entry, coordinator, key, meta))

    async_add_entities(entities)


class SystemairRegisterSensor(SystemairBaseEntity, SensorEntity):
    """Sensor backed by a Modbus register."""

    def __init__(self, entry: ConfigEntry, coordinator, reg) -> None:
        super().__init__(entry, coordinator)
        self._reg = reg

        self._attr_translation_key = reg.translation_key
        self._attr_icon = reg.icon
        self._attr_device_class = reg.device_class
        self._attr_state_class = reg.state_class
        self._attr_native_unit_of_measurement = reg.unit
        self._attr_entity_category = reg.entity_category

        # Stable unique_id across reinstall (uses entry.unique_id if set)
        self._attr_unique_id = f"{self._uid_base}_reg_{reg.key}"

    @property
    def native_value(self):
        return self.coordinator.data.get(self._reg.key)


class SystemairDerivedSensor(SystemairBaseEntity, SensorEntity):
    """Sensor derived from multiple registers."""

    def __init__(self, entry: ConfigEntry, coordinator, key: str, meta: dict) -> None:
        super().__init__(entry, coordinator)
        self._key = key
        self._meta = meta

        self._attr_translation_key = meta.get("translation_key")
        self._attr_icon = meta.get("icon")
        self._attr_device_class = meta.get("device_class")
        self._attr_state_class = meta.get("state_class")
        self._attr_native_unit_of_measurement = meta.get("unit")
        self._attr_entity_category = meta.get("entity_category")

        # Stable unique_id across reinstall (uses entry.unique_id if set)
        self._attr_unique_id = f"{self._uid_base}_derived_{key}"

    @property
    def native_value(self):
        # Derived values are computed in coordinator, stored under key
        return self.coordinator.data.get(self._key)
