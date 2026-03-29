from models.schemas import CropBatch, WeatherTelemetryInput

def evaluate_crop_rules(crop: CropBatch, weather: WeatherTelemetryInput):
    """Evaluates weather telemetry against crop biological stages."""
    sms_alert = None
    rule_name = None

    if crop.crop_type == 'Kamatis' and crop.current_stage == 'Fruiting':
        if weather.consecutive_dry_days >= 7 and weather.p_24 >= 25.0:
            rule_name = "Tomato_Fruit_Crack_Risk"
            sms_alert = (
                f"[AGRO-ALERT] Babala para sa Kamatis: "
                f"May inaasahang {weather.p_24}mm na ulan matapos ang {weather.consecutive_dry_days} araw na tag-init. "
                f"Mataas ang risk ng pagbibiyak ng bunga. - Alpha Tester"
            )
            
    return rule_name, sms_alert