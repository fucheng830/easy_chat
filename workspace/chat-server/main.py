from fastapi import FastAPI
from app.api.routers import api_router

app = FastAPI()

# 包含来自不同模块的路由器
app.include_router(api_router)
