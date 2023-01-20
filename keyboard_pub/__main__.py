from keyboard_pub import listener
from keyboard_pub.scheduling import scheduler


if __name__ == '__main__':
    scheduler.start()
    listener.start()
