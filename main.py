from fastapi import FastAPI
from pydantic import BaseModel

class parte1(BaseModel):
    parte: str
    parte2: str
    parte3: str

app=FastAPI()

@app.get("/")

def index():
    return "hola"

@app.get("/ruta/{id}")
def motrar_hoja(id):
    return {"ruta":id}

@app.post("/parte1")
def insertar(parte: parte1):
    return{"esta en la parte indicada": parte.parte2}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
