def compare(_input: tuple[str, str], message: str = "Terrible poop!"):
    first, second = _input

    assert len(first) == len(second), message

    for i, y in zip(first, second):  # i in first and y in second:
        if i == y:
            continue
        else:
            return i, y

    return True
