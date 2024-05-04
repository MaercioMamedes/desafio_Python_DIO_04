from fastapi import FastAPI
from workout_DIO.routers import api_router
from fastapi_pagination import add_pagination


app = FastAPI(title="WokroutAPI-DIO")
app.include_router(api_router)
add_pagination(app)


@app.get("/")
def get():
    return{
            "endpoint": [route.path for route in app.routes],
        }
