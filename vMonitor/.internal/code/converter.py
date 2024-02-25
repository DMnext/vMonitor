def convert(convert_message: str) -> int | bool | None:

    if convert_message.isdigit():
        return int(convert_message)

    if convert_message == "true" or convert_message == "True":
        return True

    if convert_message == "false" or convert_message == "False":
        return False
