from fastapi import FastAPI, HTTPException, Header
from typing import Annotated
import jwt
from datetime import datetime, timedelta

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
