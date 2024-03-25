import time
from queue import Queue
from threading import Thread


def worker(tasks: Queue):
    """
    Worker waits for tasks and executes them.
    """

    while True:
        task = tasks.get()

        if task is None:
            break

        print(f"Running task '{task}'!")
        time.sleep(1)

    print("Worker has finished working")


def main():

    tasks = Queue(maxsize=0xff)

    worker_thread = Thread(target=worker, name="Discord worker", args=(tasks,))
    worker_thread.start()

    tasks.put("say hello")

    print("Main thread waits 5 seconds")

    time.sleep(5)

    print("After 5 seconds")
    tasks.put("VERY HARD TASK")

    time.sleep(1)

    print("Telling worker to finish all pending tasks and stop working")

    # ask the worker to stop
    tasks.put(None)

    # wait until the worker has indeed stopped
    worker_thread.join()

    print("Main thread has waited until worker finished working.")


if __name__ == "__main__":
    main()
