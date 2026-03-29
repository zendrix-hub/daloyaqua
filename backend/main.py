from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler

# Import your separated routes and controllers
from routes import evaluation_routes
from controllers.evaluation_controller import daily_evaluation_job

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup Cron Job when server starts
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_evaluation_job, 'cron', hour=4, minute=0, timezone='Asia/Manila')
    scheduler.start()
    yield
    # Shutdown Cron Job when server stops
    scheduler.shutdown()

# Initialize App
app = FastAPI(title="Masbate Agronomic Intelligence Engine", lifespan=lifespan)

# Attach Routes
app.include_router(evaluation_routes.router, prefix="/api/v1")