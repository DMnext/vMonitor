import traceback
from abc import ABC
from typing import List


class VMError(Exception, ABC):
    """
    Base class for all vmonitor-related errors.
    """

    def __init__(self, problem_text: str, /, *,
                 is_regular: bool = False):
        super().__init__()

        self.code = 1
        self.problem_text = problem_text

        # regular errors are those that can happen if the tool is configured correctly, but has been provided invalid input
        # here, 'input' should be narrowly understood as end user input, not as the tool users' input
        # an example of such an input would be the image provided as a basis for the analysis
        # on the other hand, the template configuration file does not count as end user input
        self.is_regular = is_regular

        self._causes: List[VMError] = []
        self._external_causes: List[BaseException] = []

    def add_cause(self, cause, /):
        assert isinstance(cause, VMError)
        self._causes.append(cause)

    def get_causes(self):
        return self._causes

    def add_external_cause(self, cause: BaseException, /):
        self._external_causes.append(cause)

    def get_external_causes(self) -> List[BaseException]:
        return self._external_causes

    def get_details(self) -> str | None:
        return None

    def serialize(self):

        causes = [
            cause.serialize()
            for cause in self._causes
        ]

        return self.problem_text


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
