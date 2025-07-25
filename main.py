from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Import routes
from routes.shortlist_routes import router as shortlist_router
from routes.mail_routes import router as mail_router

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Create uploads folder if not exists
os.makedirs("uploads", exist_ok=True)

# Include routers
app.include_router(shortlist_router)
app.include_router(mail_router)

@app.get("/")
def welcome():
    return templates.TemplateResponse("welcome.html", {"request": {}})
