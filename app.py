import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create a minimal app first
from fastapi import FastAPI

app = FastAPI(
    title="Cyber Risk Assessment Backend",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Cyber Risk Intelligence Dashboard API"}

# Try to import and use the full app if available
try:
    from backend.main import app as backend_app
    # Replace the minimal app with the full one
    app = backend_app
except Exception as e:
    print(f"⚠️ Could not import backend app: {e}")
    import traceback
    traceback.print_exc()
    # Keep using the minimal app defined above

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
