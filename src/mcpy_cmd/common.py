from dataclasses import dataclass
from .util import tokens_to_str

@dataclass
class Pos:
    x: str
    y: str
    z: str

    def __str__(self) -> str:
        return tokens_to_str(self.x, self.y, self.z)
