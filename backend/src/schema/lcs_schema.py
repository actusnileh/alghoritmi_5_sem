from pydantic import BaseModel


class LCSResponse(BaseModel):
    data: list[list[int]]
