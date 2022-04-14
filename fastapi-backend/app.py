from fastapi import FastAPI


app = FastAPI()

# create a hello world route
@app.get("/")
def hello_world():
    message = "Fastapi is working."
    return {"message": message}