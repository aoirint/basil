from uuid import UUID, uuid4
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SessionAuthorizeResponse(BaseModel):
  session_id: UUID

@router.get('/sessions/authorize', response_model=SessionAuthorizeResponse)
async def authorize(username: str, password: str):
  pass

@router.get('/sessions/{session_id}/destroy')
async def destroy(session_id: UUID):
  pass
