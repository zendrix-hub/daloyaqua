from pydantic import BaseModel, Field

class WeatherTelemetryInput(BaseModel):
    t_max: float = Field(..., ge=10.0, le=50.0)
    p_24: float = Field(..., ge=0.0, le=500.0)
    rh: float = Field(..., ge=0.0, le=100.0)
    consecutive_dry_days: int = Field(..., ge=0, le=365)
    operator_name: str = Field(..., max_length=50, strip_whitespace=True)

class CropBatch(BaseModel):
    id: str
    farm_id: str
    contact_number: str
    crop_type: str
    current_stage: str