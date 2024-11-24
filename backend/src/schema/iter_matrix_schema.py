from pydantic import BaseModel


class IterMatrix(BaseModel):
    matrix: list[list[int]]
    k: list[list[int]]
    optimal_brackets: str
    steps: list[str]
