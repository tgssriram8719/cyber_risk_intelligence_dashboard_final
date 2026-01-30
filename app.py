from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create a basic app that doesn't require imports
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

# Try to import backend routes after app is created
_backend_loaded = False
try:
    from backend.main import (
        app as backend_app,
    )
    # Copy all routes from backend_app to main app
    for route in backend_app.routes:
        if route not in app.routes:
            app.routes.append(route)
    _backend_loaded = True
    print("✅ Backend app loaded successfully")
except Exception as e:
    print(f"⚠️ Backend app not available: {e}")
    _backend_loaded = False

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
