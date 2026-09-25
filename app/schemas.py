from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int
    weight: str
    goal: str
    intensity: str