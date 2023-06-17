from .util import (
tokens_to_str
)

from .common import Argument
from dataclasses import dataclass

@dataclass
class Score(Argument):
    holder: str
    objective: str

    def __str__(self) -> str:
        return tokens_to_str(self.holder, self.objective)

