import traceback, sys


def error(exc):

    formatted_lines = traceback.format_exc().splitlines()
    
    errorlines = []
    
    print("------")

    for i in formatted_lines:
        errorlines.append(i)
        print(i)
    
    print("------")

    print(f"Error at line {exc.__traceback__.tb_lineno}.")
    print("")

"""
    print("*** print_tb:")
    traceback.print_tb(exc.__traceback__, limit=1, file=sys.stdout)
    print("")
    print("*** print_exception:")
    traceback.print_exception(exc, limit=2, file=sys.stdout)
    print("")
    print("*** print_exc:")
    traceback.print_exc(limit=2, file=sys.stdout)
    print("")
    print("*** format_exc, first and last line:")
    print(formatted_lines[0])
    print(formatted_lines[-1])
    print("")
    print("*** format_exception:")
    print(repr(traceback.format_exception(exc)))
    print("")
    print("*** extract_tb:")
    print(repr(traceback.extract_tb(exc.__traceback__)))
    print("")
    print("*** format_tb:")
    print(repr(traceback.format_tb(exc.__traceback__)))
    print("")
    print("*** tb_lineno:", exc.__traceback__.tb_lineno)

"""
