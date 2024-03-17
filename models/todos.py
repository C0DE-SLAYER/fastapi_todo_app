from pydantic import BaseModel

class Todo(BaseModel):
    desc: str
    complete: bool