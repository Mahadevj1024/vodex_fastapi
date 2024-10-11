from fastapi import FastAPI
from app.routes.clock_in import router as clock_in_router
from app.routes.items import router as items_router

app = FastAPI()

app.include_router(items_router, prefix="/api", tags=["Items"])
app.include_router(clock_in_router, prefix="/api", tags=["Clock-In Records"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
