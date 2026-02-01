"""Model layer for Systemair devices."""
from __future__ import annotations

from .vtr500 import VTR500Model

MODEL_REGISTRY = {
    VTR500Model.model_id: VTR500Model,
}
