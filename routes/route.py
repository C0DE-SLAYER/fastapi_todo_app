from fastapi import APIRouter

from models.todos import Todo
from config.db import collection_name
from schema.schemes import multi_serial
from bson import ObjectId

router = APIRouter()

@router.get('/')
async def get_todos():
    todos = multi_serial(collection_name.find())
    return todos

@router.post('/')
async def create_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return 'Todo created'

@router.put('/{id}')
async def update(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return multi_serial(collection_name.find({"_id": ObjectId(id)}))

@router.delete('/{id}')
async def delete(id:str, todo: Todo):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return 'Todo deleted'