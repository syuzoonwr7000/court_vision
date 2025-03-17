from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Vue.js のビルド後の静的ファイルを提供
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")
