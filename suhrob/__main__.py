from suhrob import listener
from suhrob.scheduling import scheduler


if __name__ == '__main__':
    scheduler.start()
    listener.start()
