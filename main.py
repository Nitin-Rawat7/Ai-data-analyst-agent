from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import uuid

from utils import explain_result
from analyst import analyze_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_STORE = {}


class AskRequest(BaseModel):
    file_id: str
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files are supported.")

        df = pd.read_csv(file.file)

        file_id = str(uuid.uuid4())
        DATA_STORE[file_id] = df

        dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
        null_counts = {col: int(count) for col, count in df.isnull().sum().items()}

        return {
            "file_id": file_id,
            "columns": list(df.columns),
            "rows": int(len(df)),
            "cols": int(len(df.columns)),
            "dtypes": dtypes,
            "null_counts": null_counts,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@app.post("/ask")
async def ask_question(data: AskRequest):
    try:
        if data.file_id not in DATA_STORE:
            raise HTTPException(status_code=404, detail="Invalid file_id")

        df = DATA_STORE[data.file_id]

        analysis_result = analyze_question(df, data.question)
        explanation = explain_result(data.question, analysis_result)

        return {
            "answer": explanation,
            "analysis": analysis_result,
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process question: {str(e)}")