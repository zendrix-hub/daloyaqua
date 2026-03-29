from models.schemas import WeatherTelemetryInput

def fetch_tomorrow_io_data(lat: float, lng: float) -> WeatherTelemetryInput:
    """Fetches real-time weather data for Baleno, Masbate."""
    # Simulation data for now
    return WeatherTelemetryInput(
        t_max=34.5,
        p_24=30.2, 
        rh=85.0,
        consecutive_dry_days=8,
        operator_name="System_Cron"
    )