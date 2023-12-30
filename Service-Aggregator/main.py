from fastapi import FastAPI
from utils.AddControllers import populate_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DMS Microservices - Aggregator", docs_url="/")

origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(populate_router)