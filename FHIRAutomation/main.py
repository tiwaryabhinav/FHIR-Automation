from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.app_controller import router as controller_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(controller_router)