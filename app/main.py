from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import pandas as pd


app = FastAPI() # API endpoint

@app.get("/")
def root():
    dummy_data = {"word":"Hello world!"}
    return dummy_data

@app.get("/build")
def build():
    df = pd.read_csv("/Users/yharyarias/Documents/globant/coding_challenge_de/data/jobs.csv").T.to_dict()
    return df

@app.post("/upload")
def upload(file: UploadFile = File("/Users/yharyarias/Documents/globant/coding_challenge_de/data/jobs.csv")):
    contents = file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    buffer.close()
    file.file.close()
    return df.to_dict(orient='records')