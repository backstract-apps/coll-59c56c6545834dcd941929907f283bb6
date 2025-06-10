from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Tasks(BaseModel):
    id: Any
    description: str
    due_date: datetime.date
    status: str


class ReadTasks(BaseModel):
    id: Any
    description: str
    due_date: datetime.date
    status: str
    class Config:
        from_attributes = True


class Users(BaseModel):
    id: Any
    name: str
    contact_info: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_info: str
    class Config:
        from_attributes = True


class Assignments(BaseModel):
    id: Any
    task_id: int
    user_id: int


class ReadAssignments(BaseModel):
    id: Any
    task_id: int
    user_id: int
    class Config:
        from_attributes = True




class PostAssignments(BaseModel):
    id: int = Field(...)
    task_id: int = Field(...)
    user_id: int = Field(...)

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    id: int = Field(...)
    description: str = Field(..., max_length=100)
    due_date: Any = Field(...)
    status: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_info: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

