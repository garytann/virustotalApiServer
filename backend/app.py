from fastapi import FastAPI, File, UploadFile
import requests

API_KEY = "91835fbe8a24c0f0b2d12cab6b13024076af6c10900dbaeeca84a112747286e3"
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

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # TODO: 1) Upload file to VirusTotal
    # TODO: 2) Get analysis ID
    # TODO: 3) Return analysis ID
    # TODO: 4) Check analysis status
    # TODO: 5) Call file_analysis() to get analysis results
    
    url = "https://www.virustotal.com/api/v3/private/files"
    
    content = await file.read()

    # files = { "file": (file.filename, open(file.filename, "rb"), "application/x-javascript") }
    payload = {
        "disable_sandbox": "false",
        "enable_internet": "false",
        "intercept_tls": "false"
    }
    
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY,
    }

    # response = requests.post(url, data=payload, files=files, headers=headers)

    
    # return {"filename": file.filename, "contents": response}
    return {"filename": file, "contents": content}


