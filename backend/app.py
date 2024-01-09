from fastapi import FastAPI, File, UploadFile
import requests
import vt
import asyncio
import concurrent.futures


API_KEY = "91835fbe8a24c0f0b2d12cab6b13024076af6c10900dbaeeca84a112747286e3"

client = vt.Client(API_KEY)

app = FastAPI()

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

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # TODO: 1) Upload file to VirusTotal
    # TODO: 2) Get analysis ID
    # TODO: 3) Return analysis ID
    # TODO: 4) Check analysis status
    # TODO: 5) Call file_analysis() to get analysis results using analysis ID
    url = "https://www.virustotal.com/api/v3/files"

    files = { "file": (file.filename, file.file, "application/x-javascript") }

    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.post(url, files=files, headers=headers)
    analysis_id = response.json()['data']['id']
    result = file_analysis(analysis_id)

    print(result)
    # analysis = await client.scan_file_async(file.file, wait_for_completion=True)

    # if analysis.status == "completed":
    #     print(analysis)

    return {"filename": file.filename}


