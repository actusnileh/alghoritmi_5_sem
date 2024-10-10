from enum import Enum

from pydantic import BaseModel


class MethodSchema(Enum):
    Discrete = "Дискретный"
    Continuous = "Непрерывный"


class ElementWithWeight(BaseModel):
    weight: int
    value: int


class ElementsWithWeight(BaseModel):
    elements: list[ElementWithWeight]
