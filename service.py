from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def post_assignments(db: Session, raw_data: schemas.PostAssignments):
    id: int = raw_data.id
    task_id: int = raw_data.task_id
    user_id: int = raw_data.user_id

    record_to_be_added = {"id": id, "task_id": task_id, "user_id": user_id}
    new_assignments = models.Assignments(**record_to_be_added)
    db.add(new_assignments)
    db.commit()
    db.refresh(new_assignments)
    assignments_inserted_record = new_assignments.to_dict()

    res = {
        "assignments_inserted_record": assignments_inserted_record,
    }
    return res


async def put_assignments_id(db: Session, id: int, task_id: int, user_id: int):

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))
    assignments_edited_record = query.first()

    if assignments_edited_record:
        for key, value in {"id": id, "task_id": task_id, "user_id": user_id}.items():
            setattr(assignments_edited_record, key, value)

        db.commit()
        db.refresh(assignments_edited_record)

        assignments_edited_record = (
            assignments_edited_record.to_dict()
            if hasattr(assignments_edited_record, "to_dict")
            else vars(assignments_edited_record)
        )
    res = {
        "assignments_edited_record": assignments_edited_record,
    }
    return res


async def delete_assignments_id(db: Session, id: int):

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        assignments_deleted = record_to_delete.to_dict()
    else:
        assignments_deleted = record_to_delete
    res = {
        "assignments_deleted": assignments_deleted,
    }
    return res


async def post_file_upload(db: Session, document: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document.read()

    name = document.filename
    file_path = file_path + "/" + name

    import mimetypes

    document.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    user_file_document = file_url
    res = {
        "file_upload": user_file_document,
    }
    return res


async def get_tasks(db: Session):

    query = db.query(models.Tasks)

    tasks_all = query.all()
    tasks_all = (
        [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all
    )
    res = {
        "tasks_all": tasks_all,
    }
    return res


async def get_tasks_id(db: Session, id: int):

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))

    tasks_one = query.first()

    tasks_one = (
        (tasks_one.to_dict() if hasattr(tasks_one, "to_dict") else vars(tasks_one))
        if tasks_one
        else tasks_one
    )

    res = {
        "tasks_one": tasks_one,
    }
    return res


async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    id: int = raw_data.id
    description: str = raw_data.description
    due_date: datetime.date = raw_data.due_date
    status: str = raw_data.status

    record_to_be_added = {
        "id": id,
        "status": status,
        "due_date": due_date,
        "description": description,
    }
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks.to_dict()

    res = {
        "tasks_inserted_record": tasks_inserted_record,
    }
    return res


async def put_tasks_id(
    db: Session, id: int, description: str, due_date: str, status: str
):

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))
    tasks_edited_record = query.first()

    if tasks_edited_record:
        for key, value in {
            "id": id,
            "status": status,
            "due_date": due_date,
            "description": description,
        }.items():
            setattr(tasks_edited_record, key, value)

        db.commit()
        db.refresh(tasks_edited_record)

        tasks_edited_record = (
            tasks_edited_record.to_dict()
            if hasattr(tasks_edited_record, "to_dict")
            else vars(tasks_edited_record)
        )
    res = {
        "tasks_edited_record": tasks_edited_record,
    }
    return res


async def delete_tasks_id(db: Session, id: int):

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict()
    else:
        tasks_deleted = record_to_delete
    res = {
        "tasks_deleted": tasks_deleted,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_info: str = raw_data.contact_info

    record_to_be_added = {"id": id, "name": name, "contact_info": contact_info}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_id(db: Session, id: int, name: str, contact_info: str):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_info": contact_info,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_assignments(db: Session):

    query = db.query(models.Assignments)

    assignments_all = query.all()
    assignments_all = (
        [new_data.to_dict() for new_data in assignments_all]
        if assignments_all
        else assignments_all
    )
    res = {
        "assignments_all": assignments_all,
    }
    return res


async def get_assignments_id(db: Session, id: int):

    query = db.query(models.Assignments)
    query = query.filter(and_(models.Assignments.id == id))

    assignments_one = query.first()

    assignments_one = (
        (
            assignments_one.to_dict()
            if hasattr(assignments_one, "to_dict")
            else vars(assignments_one)
        )
        if assignments_one
        else assignments_one
    )

    res = {
        "assignments_one": assignments_one,
    }
    return res
