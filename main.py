from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class ModelData(BaseModel):
    document: str

class TestData(BaseModel):
    id:int
    message:str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/new")
async def new():
    return {"message":"new change"}
# @app.post("/predict")
# async def predict(d:ModelData):
#     nlp_updated = spacy.load('tmp_model')
#     results = nlp_updated(d.document)
#     data = {}
#     for ent in results.ents:
#         data.update({
#             ent.label_: ent.text
#         })
#     return data

@app.get("/service/{service_id}")
async def read_item(service_id: str):
    obj = {
        '1':{'Id':service_id,'Name':'Azure Static App','Type':'Compute','Usage':'Deploy static websites with no server side rendering'},
        '2':{'Id':service_id,'Name':'Azure App Service','Type':'Compute','Usage':'Deploy Wepapps, api\'s, mobile app backends etc'},
        '3':{'Id':service_id,'Name':'Azure Cosmos DB','Type':'Database','Usage':'Data at Rest Encrypted Database'},
        '4':{'Id':service_id,'Name':'Azure KeyVault','Type':'Security','Usage':'Storing keys and secrets'},
        '5':{'Id':service_id,'Name':'Azure Kubernetes Service','Type':'Compute','Usage':'Container/Microservice Orchestration service'},
        '6':{'Id':service_id,'Name':'Azure Functions','Type':'Compute','Usage':'Deploy small tasks, daily scheduled jobs, batch processing tasks'},
        '7':{'Id':service_id,'Name':'Azure Form Recognizer','Type':'Cognitive','Usage':'Extract data from forms, receipts, passports etc'},
        '8':{'Id':service_id,'Name':'Azure Virtual Machines','Type':'Compute','Usage':'Use for deploying monolithic apps with extensibility options'},
        '9':{'Id':service_id,'Name':'Azure Storage','Type':'Storage','Usage':'Store files, structured data in Blob, Queues, Tables etc'},
        '10':{'Id':service_id,'Name':'Azure Virtual Network','Type':'Security','Usage':'Helps in making deployments isolated and secure'}
    }
    if service_id not in obj.keys():
        return {'Id':service_id,'Name':'-','Type':'-','Usage':'-'}
    return obj[service_id]

@app.get("/new1")
async def new():
    return {"message":"new change 1"}

@app.post("/test")
def test(data:TestData):
    return {'message':data.message,'id':data.id}