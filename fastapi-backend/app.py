from fastapi import FastAPI

from api.routes import router as api_router


app = FastAPI(openapi_url="/fastapi/api/v1/openapi.json")



app.include_router(api_router, prefix="/api/v1")

app.mount(path="/fastapi", app=app)
