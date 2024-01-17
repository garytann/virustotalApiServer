from fastapi import FastAPI, File, UploadFile, Request
import requests
from datetime import datetime
import os
from fastapi.middleware import cors
from fastapi.encoders import jsonable_encoder


from dotenv import load_dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient

from models.file import FileModel

load_dotenv()

# GET API KEY FROM .ENV FILE
API_KEY = os.getenv("API_KEY")
URI = os.getenv("URI")
DB = os.getenv("MONGO_DB")

# client = vt.Client(API_KEY)

app = FastAPI()
# Create a new client and connect to the server
# client = MongoClient(URI, server_api=ServerApi('1'))

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    # app.mongodb_client = MongoClient(URI,server_api=ServerApi('1'))
    app.mongodb_client = AsyncIOMotorClient(URI,server_api=ServerApi('1'))
    app.database = app.mongodb_client[DB]
    try:
        app.mongodb_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return app.database

@app.on_event("shutdown")
async def shutdown_db_client():
    print("You successfully disconnected your db client!")
    app.mongodb_client.close()

def check_malicious(value : int):
    result = "malicious" if value > 0 else "not malicious"
    return result


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/analysis/{item_id}")
def file_analysis(item_id: str):
    url = f"https://www.virustotal.com/api/v3/analyses/{item_id}"

    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(url, headers=headers)

    print(response)
    return response.json()

# async def scan_file_in_thread(file):
#     loop = asyncio.get_event_loop()
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, client.scan_file, file)
#     return result

@app.get("/report/{hash_id}")
def file_report(hash_id: str):
    url = f"https://www.virustotal.com/api/v3/files/{hash_id}"

    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(url, headers=headers)

    print(response)
    return response.json()

@app.post("/upload")
async def upload_file(request : Request, file: UploadFile = File(...)):
    res = []
    # TODO: 1) Upload file to VirusTotal
    # TODO: 2) Get analysis ID
    # TODO: 3) Get hash ID
    # TODO: 4) Check analysis status
    # TODO: 5) Call file_analysis() to get analysis results using analysis ID
    # TODO: 6) Call file_report() to get report using hash ID to determine if file is malicious or not

    data = {}
    url = "https://www.virustotal.com/api/v3/files"

    files = { "file": (file.filename, file.file, "application/x-javascript") }

    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.post(url, files=files, headers=headers)
    analysis_id = response.json()['data']['id']
    analysis_result = file_analysis(analysis_id)
    hash_id = analysis_result['meta']['file_info']['sha256']
    report = file_report(hash_id) 
    
    malicious_value = report['data']['attributes']['last_analysis_stats']['malicious']

    # store the file data as a dictionary first
    data['analysis_id'] = analysis_id
    data['hash_id'] = hash_id
    data['filename'] = file.filename
    data['type'] = check_malicious(malicious_value)
    data['meta'] = report['data']
    
    # Insert the record into the database
    file_data = jsonable_encoder(data)
    file_object = await request.app.database["VirusData"].insert_one(file_data)

    print(file_object)
    
    # return the data as an array of dictionary
    res.append(data)
    # print(report['data']['attributes']['popular_threat_classification']['suggested_threat_label'])
    # print(malicious_value)
    # analysis = await client.scan_file_async(file.file, wait_for_completion=True)

    # if analysis.status == "completed":
    #     print(analysis)

    return {"data": res}


