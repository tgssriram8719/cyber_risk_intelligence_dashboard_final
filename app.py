from fastapi import FastAPI

app = FastAPI(
    title="Cyber Risk Assessment Backend",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Cyber Risk Intelligence Dashboard API", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
