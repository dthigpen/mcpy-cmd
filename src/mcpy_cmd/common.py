from abc import ABC, abstractmethod
from dataclasses import dataclass
from .util import tokens_to_str, stringify, listify


@dataclass
class Pos:
    x: str
    y: str
    z: str

    def __str__(self) -> str:
        return tokens_to_str(self.x, self.y, self.z)

@dataclass
class Argument:
    
    def __post_init__(self):
        if not self.validate():
            raise TypeError('Invalid arguments')
    
    # @abstractmethod
    def validate(self):
        return True

    @abstractmethod
    def __str__(self) -> str:
        pass

@dataclass
class Function(Argument):
    resource_location: str

    def __str__(self) -> str:
        return self.resource_location
    
class Fn(Function):
    pass

@dataclass
class Value(Argument):
    value: str

@dataclass
class StoragePath(Argument):
    namespace: str
    path: str

    def __str__(self):
        return tokens_to_str(self.namespace, self.path)
    
@dataclass
class EntityPath(Argument):
    selector: str
    path: str

    def __str__(self):
        return tokens_to_str(self.namespace, self.path)

@dataclass
class BlockPath(Argument):
    pos: str
    path: str

    def __str__(self):
        return tokens_to_str(self.pos, self.path)

def get_target_type(target: EntityPath | StoragePath | BlockPath | Value):
    '''Gets the string representation of the class type to be used in commands'''
    if isinstance(target, EntityPath):
        return 'entity'
    elif isinstance(target, StoragePath):
        return 'storage'
    elif isinstance(target, BlockPath):
        return 'block'
    elif isinstance(target, Value) or isinstance(target, str):
        return 'value'
    else:
        raise ValueError(f'Unsupported target type: {type(target)}')
        # return None
        
        
