from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
]

# Configuracion de CORS para ejecutar la aplicación desde diferentes puertos de ejecución
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar directorio estático para agregar archivos como img, CSS, SAAS, JS, etc...
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar plantillas Jinja2 para mostrar el template
templates = Jinja2Templates(directory="templates")

# Configuramos los que podemos recibir o enviar por medio de un Objeto
class Datos(BaseModel):
    year: str
    area: str
    producto: str
    actividad: str
    etapa: str


# Declaramos las funciones con los métodos de REQUEST de FastAPI, como get, post, delete...
# Las asociamos a un ENDPOINT

# Al primer get lo asociamos a la vista para mostrar el template con el archivo index.html
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Método POST donde vamos a recibir los datos que el usuario nos proporcionara, para convertirlos
# en variables para que el modelo lo analice.
@app.post("/datos")
async def datosPost(datos: Datos):

    if datos.year == '2022':
        return {"prediccion": "muy alta"}
    elif datos.year == '2020':
        return {"prediccion": "alta"}
    elif datos.year == '2018':
        return {"prediccion": "baja"}
    elif datos.year == '2016':
        return {"prediccion": "muy baja"}
    
    
