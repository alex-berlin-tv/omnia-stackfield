from .config import settings

import uvicorn

def app():
    uvicorn.run(
        "gaia.server:app",
        port=settings.port
    )