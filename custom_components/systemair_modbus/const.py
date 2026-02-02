"""Constants for Systemair Modbus integration."""
from __future__ import annotations

DOMAIN = "systemair_modbus"

CONF_HOST = "host"
CONF_PORT = "port"
CONF_SLAVE = "slave"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_MODEL = "model"

DEFAULT_PORT = 502
DEFAULT_SLAVE = 1
DEFAULT_SCAN_INTERVAL = 10  # seconds

PLATFORMS: list[str] = ["sensor", "binary_sensor", "switch", "select", "number", "climate", "button"]

# Modell-IDer må matche models/*.py
MODEL_SAVE = "save"
SUPPORTED_MODELS = [MODEL_SAVE]

