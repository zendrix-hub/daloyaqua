import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Centralized environment variables
TOMORROW_IO_API_KEY = os.getenv("TOMORROW_IO_API_KEY", "mock_weather_key")
SEMAPHORE_API_KEY = os.getenv("SEMAPHORE_API_KEY", "mock_sms_key")
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://mock.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "mock_service_key")