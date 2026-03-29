from datetime import datetime
from config.db_config import supabase
from models.schemas import CropBatch
from services.weather_service import fetch_tomorrow_io_data
from services.rules_service import evaluate_crop_rules
from services.sms_service import dispatch_semaphore_sms

def daily_evaluation_job():
    print(f"[{datetime.now()}] Waking up: Starting daily agronomic evaluation...")
    
    # 1. Fetch Weather
    baleno_weather = fetch_tomorrow_io_data(12.3500, 123.5167)
    
    # 2. Fetch Active Crop Batches from DB
    try:
        response = supabase.table('crop_batches').select('id, crop_type, current_stage, farm_id, farms(contact_number)').execute()
        db_batches = response.data
    except Exception as e:
        print(f"❌ [DATABASE ERROR]: {e}")
        db_batches = []
    
    # 3. Evaluate Rules & Dispatch Alerts
    for row in db_batches:
        batch = CropBatch(
            id=row['id'],
            farm_id=row['farm_id'],
            contact_number=row['farms']['contact_number'],
            crop_type=row['crop_type'],
            current_stage=row['current_stage']
        )
        
        rule_triggered, sms_content = evaluate_crop_rules(batch, baleno_weather)
        
        if sms_content:
            success = dispatch_semaphore_sms(batch.contact_number, sms_content)
            if success:
                # Log success to DB
                supabase.table('alert_dispatches').insert({
                    "batch_id": batch.id,
                    "rule_triggered": rule_triggered,
                    "sms_content": sms_content
                }).execute()
                print(f"    Logged {rule_triggered} to database.")