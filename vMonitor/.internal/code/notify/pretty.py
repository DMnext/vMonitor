from rich.syntax import Syntax
from rich.console import Console

console = Console()


def pretty_syntax(code, code_name):
    syntax = Syntax(code, code_name, indent_guides=True, line_numbers=True)
    console.print(syntax)


def errorhandle(err, errormessage):
    console.print_exception(extra_lines=5)
    print(errormessage)
    exit(1)
