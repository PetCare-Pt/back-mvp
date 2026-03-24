from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.pro_profiles import pp_router
from routers.pets_profiles import pep_router
import firebase_admin
from firebase_admin import credentials
import os

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred)

app = FastAPI(title="Pet Care API", version="1.0.0", description="Pet Care API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(pp_router, prefix="/api/v1")
app.include_router(pep_router, prefix="/api/v1")
