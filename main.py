from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.diagnosis import router as diagnosis_router
from routes.weather import router as weather_router
from routes.market import router as market_router

from routes.chat import router as chat_router



app = FastAPI(title="AI Farm Companion")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(diagnosis_router)
app.include_router(weather_router)
app.include_router(market_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Backend Running"}