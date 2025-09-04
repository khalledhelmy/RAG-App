from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = 'File validate successfully'
    FILE_TYPE_NOT_SUPPORTED = 'File type not supported'
    FILE_SIZE_EXCEEDED = 'File size exceeded'
    FILE_UPLOAD_SUCCESS = 'File Upload success'
    FILE_UPLOAD_FAILED = 'File Upload failed'
    PROCESSING_FAILED = 'Processing Failed'
    PROCESSING_SUCCESS = 'Processing Success'
    NO_FILES_ERROR = 'Not Found Files'
    FILE_ID_ERROR = 'No file found with this id'
    PROJECT_NOT_FOUND_ERROR = "project_not_found"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"