from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "Base sye"
    }]
)

app.include_router(user)