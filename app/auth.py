from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

router = APIRouter()

# Temporary user storage
users = []


@router.post("/register")
def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    username = username.strip()
    email = email.strip().lower()
    password = password.strip()

    if len(username) < 3:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Username must contain at least 3 characters"
            }
        )

    if "@" not in email or "." not in email:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Please enter a valid email address"
            }
        )

    if len(password) < 6:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Password must contain at least 6 characters"
            }
        )

    for user in users:
        if user["email"] == email:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Email already registered"
                }
            )

    new_user = {
        "username": username,
        "email": email,
        "password": password
    }

    users.append(new_user)

    return {
        "success": True,
        "message": "Registration successful",
        "user": {
            "username": username,
            "email": email
        }
    }


@router.post("/login")
def login_user(
    email: str = Form(...),
    password: str = Form(...)
):
    email = email.strip().lower()
    password = password.strip()

    for user in users:
        if user["email"] == email and user["password"] == password:
            return {
                "success": True,
                "message": "Login successful",
                "user": {
                    "username": user["username"],
                    "email": user["email"]
                }
            }

    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": "Invalid email or password"
        }
    )