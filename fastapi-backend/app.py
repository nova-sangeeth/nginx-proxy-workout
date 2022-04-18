from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# create a hello world route
@app.get("/fastapi/api")
def hello_world():
    message = "Fastapi is working."
    return {"message": message}

# function to render a html template.
@app.get("/fastapi/html")
def html_template():
    return HTMLResponse("""
    <html>
        <head>
            <title>Fastapi-server</title>
        </head>
        <body>
            <h1>Fastapi is server is up.</h1>
        </body>
    </html>

    """)
