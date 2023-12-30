from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class ProcessTime(BaseHTTPMiddleware):
    async def dispatch(self,request:Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["Processing-Time"] = str(process_time)
        return response