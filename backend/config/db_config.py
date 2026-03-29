from supabase import create_client, Client
from config.env_config import SUPABASE_URL, SUPABASE_KEY

# Initialize Supabase Client globally so other files can import it
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)