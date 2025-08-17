from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix='/api/v0'
)

@base_router.get('/')
async def Home():
    app_name = os.getenv('APP_NAME')
    app_ver = os.getenv('APP_VERSION')
    return {
        'App Name': app_name,
        'App Version': app_ver
    }