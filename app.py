from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Указываем правильную директорию для статических файлов и шаблонов
app.mount("/static", StaticFiles(directory="static"), name="static")
index = Jinja2Templates(directory="templates")  # Путь к директории с шаблонами

@app.get("/", response_class=HTMLResponse)
async def page_slash_home(request: Request):
    return index.TemplateResponse("index.html", {"request": request})  # Изменяем порядок аргументов

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=80, host="163.5.120.161")
