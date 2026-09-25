from fastapi import APIRouter, Form
from .gemini_generator import generate_fitness_plan

router = APIRouter()


@router.post("/generate")
def generate_plan(
    name: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    plan = generate_fitness_plan(
        age,
        weight,
        goal,
        intensity
    )

    return {
        "success": True,
        "name": name,
        "plan": plan
    }