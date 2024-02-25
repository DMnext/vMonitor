def compare(_input: tuple[str, str]):
    first, second = _input

    for i in first and y in second:
        if i == y:
            continue
        else:
            return i, y

    return True
