from fastapi import FastAPI
from routes import router
from config import DEBUG_MODE

app = FastAPI()

# Include the API routes
app.include_router(router)

# Raise an exception if DEBUG mode is disabled, indicating the feature isn't ready for production
if not DEBUG_MODE:
    @app.on_event("startup")
    def startup_event():
        raise Exception("Feature is not ready for live yet")