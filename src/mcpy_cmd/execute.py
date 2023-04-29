from .util import RootCmd, SubCmd, BaseCmd, EndCmd, tokens_to_str
from enum import Enum

def Execute():
    return ExecuteCmd(RootCmd(''))

class Anchor(Enum):
    EYES = 0
    FEET = 1

class ExecuteCmd(SubCmd):

    def __init__(self, parent: BaseCmd | str, *args, **kwargs) -> None:
        super().__init__(parent, '',*args, **kwargs)

    def align(self, axes: str):
        sub = SubCmd(self, ['align $axes'], template_args={'axes':axes})
        return ExecuteCmd(sub)
    
    def anchored(self, anchor: Anchor):
        if not isinstance(anchor, Anchor):
            raise ValueError(f'Invalid anchor: {anchor}')
        anchor_str = 'eyes' if anchor == Anchor.EYES else 'feet'
        sub = SubCmd(self, ['anchor $anchor'], template_args={'anchor': anchor_str})
        return ExecuteCmd(sub)

    def run(self, cmd: EndCmd | str):
        return tokens_to_str('execute', EndCmd(self, ['run', str(cmd)]))
