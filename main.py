from fastapi import FastAPI

app = FastAPI(title="Production API Pipeline")

@app.get("/")
def read_root():
    return {"status": "success", "message": "API is live and running!"}

@app.get("/health")
def health_check():
    return {"health": "100%", "system": "operational"}