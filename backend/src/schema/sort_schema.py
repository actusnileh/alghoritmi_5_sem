from pydantic import BaseModel


class TimingSort(BaseModel):
    name: str
    massive: int
    time: float


class TimingsSort(BaseModel):
    data: list[TimingSort]
