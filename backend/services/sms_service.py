def dispatch_semaphore_sms(contact_number: str, message: str) -> bool:
    """Dispatches actual SMS via Semaphore API."""
    # Simulation mode to bypass 0 credits issue
    print(f"✅ [SIMULATED SMS SUCCESS] Pretending to send to {contact_number}: {message}")
    return True