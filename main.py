from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


class TestModel(BaseModel):
    name: str
    surname: str
    age: int
    email: str
    description: str | None = None

class ModelName(str, Enum):
    patient = 'patient'
    admin = 'admin'
    owner = 'owner'

app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    return {'model': model_name}

@app.get('/file/{file_path:path}')
def read_file(file_path: str):
    return {'file path': file_path}


@app.get('/items/{item_id}')
def home(item_id: int):
    return {'message': f'hello world { item_id }'}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.post('/testmodel')
def pydanticTest(item: TestModel):
    return {'item': item}
