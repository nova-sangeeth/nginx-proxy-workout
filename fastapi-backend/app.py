from fastapi import FastAPI


app = FastAPI()

# create a hello world route
@app.get("/fastapi/api")
def hello_world():
    message = "Fastapi is working."
    return {"message": message}