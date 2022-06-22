from uuid import UUID
from fastapi import FastAPI
import jwt
from http_models import *
import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET = os.environ['JWT_SECRET']

app = FastAPI()

class Token(BaseModel):
  sub: UUID
  exp: int

def create_token() -> Token:
  return Token(
    sub=user_id,
    exp=exp,
  )

def validate_token() -> bool:
  return False

@app.get('/authorize')
async def authorize(username: str, password: str) -> str:
  token_string = jwt.encode(token.dict(), JWT_SECRET, 'HS256')
  return token_string

@app.get('/posts')
async def get_public_posts():
  pass

@app.get('/user/{user_id}/posts')
async def get_user_posts(user_id: UUID):
  pass

@app.get('/user/{user_id}/posts')
async def get_user_posts(user_id: UUID):
  pass
