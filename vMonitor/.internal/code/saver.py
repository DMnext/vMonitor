from system import get_system_info
import os

info = get_system_info()


def save_log_line(line_contents, file_name):
    # Open a file in write mode ("w")
    with open(file_name, "a") as file:
        # Write lines to the file
        file.write(f"{line_contents}\n")


def prepare_to_save_log(file_name, rid):
    fh = open(file_name, "w")
    fh.write(f"vMonitorLOG[{rid}]\n{info}\n")
    fh.close()
