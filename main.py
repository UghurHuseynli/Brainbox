from enum import Enum
from fastapi import FastAPI

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
