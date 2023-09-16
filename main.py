from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

'''
Path Parameters
'''
@app.get("/result/{value}")
async def result_value(value : int):
    return {"message":"We can have method with type and without also her the path parameters value is: "+ str(value)}

'''
Class
'''
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


'''
Path Parameter Class object
'''
@app.get("/enum/{value}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message":"Deep learning FTW!"}
    if model_name.value == 'resnet':
        return {"model_name":model_name, "message":"LeCNN all the images"}
    return {"model_name":model_name, "message":"Have some residuals"}

'''
Query Parameter
'''
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def read_item(skip:int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]