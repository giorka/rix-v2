from fastapi import Depends
from fastapi.security import APIKeyCookie

# Token extraction marker for FastAPI Swagger UI.
# The actual token processing will be handled behind the FastAPI Token Handler.
DependsToken = Depends(APIKeyCookie(name='Authorization', auto_error=False))


__all__ = ['DependsToken']
