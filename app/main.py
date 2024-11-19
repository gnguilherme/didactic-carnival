from fastapi import FastAPI

from app.api.v1 import conversational

app = FastAPI()

# Include the conversation router
app.include_router(conversational.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Conversational API!"}
