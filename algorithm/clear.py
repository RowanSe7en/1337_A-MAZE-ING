import os
import sys


def clear(is_ft_printable: bool = True) -> None:
    """
    Clear the terminal screen in a cross-platform way.

    This function detects the operating system and runs the appropriate
    terminal command to clear the console. If the maze is too small to
    display the "42" pattern, a warning message is shown.

    Args:
        is_ft_printable: Indicates whether the maze is large enough to
            render the "42" pattern.
    """
    if sys.platform.startswith("linux") or sys.platform == "darwin":
        os.system("clear")
    elif sys.platform in ("win32", "cygwin"):
        os.system("cls")

    if not is_ft_printable:
        print(
            "The 42 pattern cannot be generated due to the coordinates"
            " passed, try different ones larger then (6, 8)."
        )
