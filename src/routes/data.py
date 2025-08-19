from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import aiofiles
import os
import logging

logger = logging.getLogger('uvicorn.errors')

data_router = APIRouter(
    prefix='/api/v0/data',
    tags=['api_v0', 'data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):
    data_controller = DataController()
    is_valid, result_sig = data_controller.validate_upload_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal': result_sig
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id  = data_controller.generate_unique_filepath(orig_file_name=file.filename, # type: ignore
                                                           project_id=project_id)

    try:
        async with aiofiles.open(file_path, 'wb') as f: # type: ignore
            while chunck := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE): # type: ignore
                await file.write(chunck)
    except Exception as e:
         logger.error(f'Error while uploading file: {e}')
         return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal': ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
        
    return JSONResponse(
            content={
                'signal': ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                'file_id': file_id
            }
    )