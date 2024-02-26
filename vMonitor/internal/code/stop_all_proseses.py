from notify_system import _communicate


def stop(msg, code):
    _communicate(msg=msg)
    exit(code)


def force_stop():
    exit(1)


def emergensy_stop():
    raise Exception()
