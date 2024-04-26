from fastapi import FastAPI
from workout_DIO.routers import api_router


app = FastAPI(title="WokroutAPI-DIO")
app.include_router(api_router)
