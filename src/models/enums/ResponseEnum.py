from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = 'File validate successfully'
    FILE_TYPE_NOT_SUPPORTED = 'File type not supported'
    FILE_SIZE_EXCEEDED = 'File size exceeded'
    FILE_UPLOAD_SUCCESS = 'File Upload success'
    FILE_UPLOAD_FAILED = 'File Upload failed'
    PROCESSING_FAILED = 'Processing Failed'
    PROCESSING_SUCCESS = 'Processing Success'
    