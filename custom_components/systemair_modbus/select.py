"""Select platform for Systemair Modbus."""
from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN
from .entity import SystemairBaseEntity

# NOTE: value mappings are taken from model constants


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    client = data["client"]
    model = data["model"]

    entities: list[SelectEntity] = [
        ModeSelect(entry, coordinator, client, model),
        ManualSpeedSelect(entry, coordinator, client, model),
        FreeCoolingMinSafSelect(entry, coordinator, client, model),
        FreeCoolingMinEafSelect(entry, coordinator, client, model),
    ]
    async_add_entities(entities)


class ModeSelect(SystemairBaseEntity, SelectEntity):
    _attr_entity_category = EntityCategory.CONFIG
    _attr_translation_key = "mode_select"
    _attr_icon = "mdi:fan"

    def __init__(self, entry: ConfigEntry, coordinator, client, model) -> None:
        super().__init__(entry, coordinator)
        self._client = client
        self._model = model
        self._attr_unique_id = f"{self._uid_base}_mode_select"
        self._attr_options = list(self._model.MODE_MAP.keys())

    @property
    def current_option(self) -> str | None:
        raw = self.coordinator.data.get("mode")
        return self._model.MODE_INV_MAP.get(raw)

    async def async_select_option(self, option: str) -> None:
        value = self._model.MODE_MAP[option]
        await self._client.write_register(self._model.ADDR_MODE, value)
        await self.coordinator.async_request_refresh()


class ManualSpeedSelect(SystemairBaseEntity, SelectEntity):
    _attr_entity_category = EntityCategory.CONFIG
    _attr_translation_key = "manual_speed_select"
    _attr_icon = "mdi:speedometer"

    def __init__(self, entry: ConfigEntry, coordinator, client, model) -> None:
        super().__init__(entry, coordinator)
        self._client = client
        self._model = model
        self._attr_unique_id = f"{self._uid_base}_manual_speed_select"
        self._attr_options = list(self._model.MANUAL_SPEED_MAP.keys())

    @property
    def current_option(self) -> str | None:
        raw = self.coordinator.data.get("manual_speed")
        return self._model.MANUAL_SPEED_INV_MAP.get(raw)

    async def async_select_option(self, option: str) -> None:
        value = self._model.MANUAL_SPEED_MAP[option]
        await self._client.write_register(self._model.ADDR_MANUAL_SPEED, value)
        await self.coordinator.async_request_refresh()


class FreeCoolingMinSafSelect(SystemairBaseEntity, SelectEntity):
    _attr_entity_category = EntityCategory.CONFIG
    _attr_translation_key = "free_cooling_min_saf_select"
    _attr_icon = "mdi:fan-speed-1"

    def __init__(self, entry: ConfigEntry, coordinator, client, model) -> None:
        super().__init__(entry, coordinator)
        self._client = client
        self._model = model
        self._attr_unique_id = f"{self._uid_base}_fc_min_saf_select"
        self._attr_options = list(self._model.FC_MIN_SPEED_MAP.keys())

    @property
    def current_option(self) -> str | None:
        raw = self.coordinator.data.get("free_cooling_min_saf")
        return self._model.FC_MIN_SPEED_INV_MAP.get(raw)

    async def async_select_option(self, option: str) -> None:
        value = self._model.FC_MIN_SPEED_MAP[option]
        await self._client.write_register(self._model.ADDR_FREE_COOLING_MIN_SAF, value)
        await self.coordinator.async_request_refresh()


class FreeCoolingMinEafSelect(SystemairBaseEntity, SelectEntity):
    _attr_entity_category = EntityCategory.CONFIG
    _attr_translation_key = "free_cooling_min_eaf_select"
    _attr_icon = "mdi:fan-speed-1"

    def __init__(self, entry: ConfigEntry, coordinator, client, model) -> None:
        super().__init__(entry, coordinator)
        self._client = client
        self._model = model
        self._attr_unique_id = f"{self._uid_base}_fc_min_eaf_select"
        self._attr_options = list(self._model.FC_MIN_SPEED_MAP.keys())

    @property
    def current_option(self) -> str | None:
        raw = self.coordinator.data.get("free_cooling_min_eaf")
        return self._model.FC_MIN_SPEED_INV_MAP.get(raw)

    async def async_select_option(self, option: str) -> None:
        value = self._model.FC_MIN_SPEED_MAP[option]
        await self._client.write_register(self._model.ADDR_FREE_COOLING_MIN_EAF, value)
        await self.coordinator.async_request_refresh()
