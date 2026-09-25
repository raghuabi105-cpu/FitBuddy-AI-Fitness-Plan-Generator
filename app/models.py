from sqlalchemy import Column, Integer, String, Text
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(String)
    goal = Column(String)
    intensity = Column(String)
    workout_plan = Column(Text)
    nutrition_tips = Column(Text)