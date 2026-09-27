from fastapi import FastAPI

app = FastAPI(
    title="RAG Engineering Platform",
    description="Advanced RAG platform built from scratch",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": "RAG Engineering Platform"
    }