from pydantic import BaseModel


class LCSResponse(BaseModel):
    elements: list[list[int]]
    directions: list[list[str]]
    all_lcs: list[str]
