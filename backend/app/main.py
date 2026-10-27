from fastapi import FastAPI

app = FastAPI(
    title="CNC Production Loss Analyzer",
    description="Manufacturing production and downtime analytics API",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "CNC Production Loss Analyzer API is running",
    }