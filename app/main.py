from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .routes import router
from .auth import router as auth_router

from pathlib import Path


app = FastAPI(title="FitBuddy AI Fitness Planner")


BASE_DIR = Path(__file__).resolve().parent.parent


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


# Existing fitness routes
app.include_router(router)

# Registration and Login API routes
app.include_router(auth_router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )


@app.post("/generate")
def generate_plan(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    from .gemini_generator import generate_fitness_plan

    plan = generate_fitness_plan(
        age,
        weight,
        goal,
        intensity
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "plan": plan
        }
    )