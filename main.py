from fastapi import FastAPI

app = FastAPI()

@app.get("/status", status_code=204)
def read_root():
    return {"Hello": "World"}

@app.get('/info')
def read_root():
    return {'url' : {'localhost:8000'}}

@app.delete('/security', status_code=401)
def read_root():
    return {'datom' : 'api'}