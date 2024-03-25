from notify.send_discord import send
from queue import Queue
from threading import Thread

tasks = Queue(maxsize=0xff)

worker_thread = Thread(target=send, name="Discord worker", args=(tasks,))
worker_thread.start()


def stop_discord_worker():
    global tasks

    tasks.put((None, None, None))
    worker_thread.join()

    return True


def send_discord(message, main_channle_msg: str, only_log: bool = False):
    global tasks

    tasks.put((message, main_channle_msg, only_log))


def send_notification(message):
    from notify.notification import send_notification

    # Example usage
    send_notification("vMonitor", f"{message}")

# .
