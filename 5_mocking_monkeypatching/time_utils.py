from datetime import datetime

def is_past_deadline(deadline: datetime) -> bool:
    now = datetime.now()
    return now > deadline
