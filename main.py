from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'datom', 'api'}

@app.get("/status", status_code=204)
def read_root():
    return 

@app.get('/info')
def read_root():
    return {'url' : {'https://datom-api.herokuapp.com'}}

@app.delete('/security', status_code=401)
def read_root():
    return 