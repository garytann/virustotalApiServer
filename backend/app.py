from fastapi import FastAPI, File, UploadFile
import requests
import asyncio
import concurrent.futures
from datetime import datetime


API_KEY = "91835fbe8a24c0f0b2d12cab6b13024076af6c10900dbaeeca84a112747286e3"

# client = vt.Client(API_KEY)

app = FastAPI()

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
async def upload_file(file: UploadFile = File(...)):

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


    data['analysis_id'] = analysis_id
    data['hash_id'] = hash_id
    data['filename'] = file.filename
    data['type'] = check_malicious(malicious_value)
    data['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['meta'] = report['data']

    # print(report['data']['attributes']['popular_threat_classification']['suggested_threat_label'])
    # print(malicious_value)
    # analysis = await client.scan_file_async(file.file, wait_for_completion=True)

    # if analysis.status == "completed":
    #     print(analysis)

    return {"data": data}


