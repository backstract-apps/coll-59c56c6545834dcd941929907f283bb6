from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/assignments/')
async def post_assignments(raw_data: schemas.PostAssignments, db: Session = Depends(get_db)):
    try:
        return await service.post_assignments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/assignments/id/')
async def put_assignments_id(id: int, task_id: int, user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_assignments_id(db, id, task_id, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/assignments/id')
async def delete_assignments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_assignments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/file_upload')
async def post_file_upload(document: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_file_upload(db, document)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(id: int, description: Annotated[str, Query(max_length=100)], due_date: str, status: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, id, description, due_date, status)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], contact_info: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, contact_info)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/assignments/')
async def get_assignments(db: Session = Depends(get_db)):
    try:
        return await service.get_assignments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/assignments/id')
async def get_assignments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_assignments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

