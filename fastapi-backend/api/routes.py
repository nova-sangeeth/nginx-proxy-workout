from email import message
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request, Response, status
from crud.base import Store

router = APIRouter()


@router.get("/hello_world")
def hello_world():
    message = "Fastapi is working."
    return {"message": message}

@router.get("/store")
def new_router():
    message = Store
    return message

@router.get("/")
def html_template(request: Request):
    return HTMLResponse(f"""
    <html>
        <head>
            <title>Fastapi-server</title>
        </head>
        <body>
            <center>
                <h1>Fastapi-server</h1>
                <h1>request: {request.url}</h1>
            </center>
        </body>
    </html>
    """) ,
