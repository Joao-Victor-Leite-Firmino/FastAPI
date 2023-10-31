from fastapi import FastAPI

app = FastAPI()

@app.get("/model_version")
async def get_info() -> dict:
    model_name = "YOLO NAS"
    version = "1.0"

    return {
        "name": model_name,
        "version": version
}