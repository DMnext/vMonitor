import os


def start():
    os.system("source venv/bin/activate && cd vMonitor/.internal/code/ && python main.py")
    os.system("cd .. && cd .. && cd ..")


if __name__ == '__main__':
    start()
