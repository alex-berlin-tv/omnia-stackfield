from .config import settings
from .stackfield import Stackfield

import uvicorn

def app():
    uvicorn.run(
        "gaia.server:app",
        port=settings.port
    )