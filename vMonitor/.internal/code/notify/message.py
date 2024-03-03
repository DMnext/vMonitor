from notify._discord import send
import time
from queue import Queue
from threading import Thread
from error import error


def send_discord(message, main_channle_msg: str, only_log: bool = False):
    
    tasks = Queue(maxsize=0xff)

    worker_thread = Thread(target=send, name="Discord worker", args=(tasks,))
    worker_thread.start()

    try:
        tasks.put((message, main_channle_msg, only_log))
    except Exception as err:
        tasks.join()
        error()
        

def send_notification(message):
    from notify.notification import send_notification

    # Example usage
    send_notification("vMonitor", f"{message}")

# .
