from .main import app

if __name__ == "main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)