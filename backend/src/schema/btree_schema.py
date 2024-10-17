from pydantic import BaseModel


class KeyValuePair(BaseModel):
    key: int
    value: int


class BTreeResponse(BaseModel):
    keys: list[KeyValuePair]
