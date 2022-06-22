
from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel


class Channel(BaseModel):
  id: UUID
  name: str

class Category(BaseModel):
  id: UUID
  name: str

class Tag(BaseModel):
  id: UUID
  name: str

class Transformer(BaseModel):
  id: UUID
  name: str

class Template(BaseModel):
  id: UUID
  name: str
  transformers: List[Transformer]

class Post(BaseModel):
  id: UUID
  title: str
  body: str
  template: Template
  channels: List[Channel]
  categories: List[Category]
  tags: List[Tag]
  unlisted: bool
  created_at: datetime
  updated_at: datetime

class User(BaseModel):
  id: UUID
  name: str
  created_at: datetime
  updated_at: datetime
