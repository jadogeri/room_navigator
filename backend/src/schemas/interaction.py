from dataclasses import dataclass
from typing import Optional

@dataclass
class InteractionResult:
    message: str
    damage_dealt: int = 0
    is_hostile: bool = True
    status_effect: Optional[str] = None
    