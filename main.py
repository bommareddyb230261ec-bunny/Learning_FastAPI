from fastapi import FastAPI

app= FastAPI()

@app.get('/home')
def greet():
    return {"Message":"From The Fast API"}
