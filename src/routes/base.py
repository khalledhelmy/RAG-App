from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix='/api/v0',
    tags=['api_v0']
)

@base_router.get('/')
async def Home(app_settings: Settings = Depends(get_settings)):
    
    app_name = app_settings.APP_NAME
    app_ver = app_settings.APP_VERSION
    return {
        'App Name': app_name,
        'App Version': app_ver
    }