import warnings
warnings.filterwarnings('ignore')

import io
import os
from fastapi import FastAPI
import pandas as pd

from app.helpers.helper import *

app = FastAPI(
    title='Sample-app FastAPI and Docker',
    version = '1.0.0'
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def ping():
    return "Hello, I am alive..."

@app.post("/process_dict")
async def process_dict(input_dict: dict):
    # You can perform any processing on the input dictionary here
    # For example, let's just return the received dictionary as is
    return input_dict