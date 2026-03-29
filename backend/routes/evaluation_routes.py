"""
routes/evaluation_routes.py
Maps URL endpoints to controller functions.
Strictly handles the HTTP request/response layer.
"""
from fastapi import APIRouter
from controllers.evaluation_controller import daily_evaluation_job
from models.schemas import WeatherTelemetryInput

# Create a FastAPI router with tags for clean Swagger UI documentation
router = APIRouter(tags=["Evaluation Engine"])

@router.post("/trigger-evaluation", summary="Manually trigger the evaluation pipeline")
def manual_trigger():
    """
    Endpoint to manually trigger the cron workflow for testing.
    Delegates the orchestration and business logic to the evaluation controller.
    """
    daily_evaluation_job()
    return {"status": "success", "message": "Evaluation pipeline triggered successfully."}

@router.post("/test-validation", summary="Test Pydantic input validation")
def test_input_validation(data: WeatherTelemetryInput):
    """
    Testing Countermeasure #4 (XSS/Injection protection via Pydantic).
    Automatically validates the incoming payload against the WeatherTelemetryInput schema.
    """
    return {"status": "valid", "data": data}