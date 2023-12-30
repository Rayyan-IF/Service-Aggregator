from fastapi import FastAPI
from src.api.middlewares import ProcessingTime
from fastapi.middleware.cors import CORSMiddleware
from src.utils.AddControllers import populate_router
from src.utils.AddEntitiesEngine import addentitiesengine

app = FastAPI(title="DMS Microservices - General",docs_url="/")

# utilized for incoming request from Front End / API Gateway
origins = ["http://localhost:3000"]

# utilized for managing the middlewares
app.add_middleware(ProcessingTime.ProcessTime)
#app.add_middleware(RouterLoggingMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

#add the entities engine automatically
addentitiesengine(False) # please set False for default mode, if you need to migrate, then change to True

#including the router
app.include_router(populate_router)