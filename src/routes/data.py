from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
from models import ResponseSignal
from .schemes.data import ProcessRequest
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
                await f.write(chunck)
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

@data_router.post('/process/{project_id}')
async def process_endpoint(project_id: str, response_request: ProcessRequest):
    file_id = response_request.file_id
    chunk_size = response_request.chunk_size
    overlap_size = response_request.overlap_size
    
    process_controller = ProcessController(project_id=project_id)

    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks = process_controller.process_file_content(file_id=file_id,
                                                          file_content=file_content,
                                                          chunk_size=chunk_size,
                                                          overlap_size=overlap_size)

    if file_chunks is None or len(file_chunks) == 0:
        JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content= {
                'signal': ResponseSignal.PROCESSING_FAILED.value
            }
        )

    return file_chunks
    