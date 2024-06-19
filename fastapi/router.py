from fastapi import FastAPI, APIRouter


def same_function():
    return "same value"

app = FastAPI()


router = APIRouter()

@app.route("/get_app")
async def route_to_app():
    return same_function()

@router.route("/get_router")
async def route_to_router():
    return same_function()
