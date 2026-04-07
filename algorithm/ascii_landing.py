import algorithm


class Color:
    """
    Utility class containing ANSI escape
    codes for terminal text styling.

    Provides constants for text formatting
    (bold, dim) and common foreground
    colors used to render the ASCII landing
    banner and other CLI elements.
    """
    reset: str = "\033[0m"
    bold: str = "\033[1m"
    dim: str = "\033[2m"

    red: str = "\033[31m"
    green: str = "\033[32m"
    yellow: str = "\033[33m"
    blue: str = "\033[34m"
    magenta: str = "\033[35m"
    cyan: str = "\033[36m"
    white: str = "\033[37m"


def ascii_landing() -> None:
    """Display the ASCII landing banner."""
    algorithm.clear()

    print(
        f"{Color.cyan}{Color.dim}\n"
        "    ╔══════════════════════════════════════════════════"
        "══════════════════════════════╗\n"
        "    ║                                                "
        "                                ║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "      █████╗     ███╗   ███╗ █████╗ ███████╗███████╗"
        f"    ██╗███╗   ██╗ ██████╗   {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "     ██╔══██╗    ████╗ ████║██╔══██╗╚══███╔╝██╔════╝"
        f"    ██║████╗  ██║██╔════╝   {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "     ███████║    ██╔████╔██║███████║  ███╔╝ █████╗  "
        f"    ██║██╔██╗ ██║██║  ███╗  {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "     ██╔══██║    ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  "
        f"    ██║██║╚██╗██║██║   ██║  {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "     ██║  ██║    ██║ ╚═╝ ██║██║  ██║███████╗███████╗"
        f"    ██║██║ ╚████║╚██████╔╝  {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.magenta}{Color.bold}"
        "     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝"
        f"    ╚═╝╚═╝  ╚═══╝ ╚═════╝   {Color.cyan}{Color.dim}║\n"
        "    ║                                                 "
        "                               ║\n"
        f"    ║{Color.yellow}{Color.bold}"
        "                           🧩  A - M A Z E - I N G  🧩"
        f"                          {Color.cyan}{Color.dim}║\n"
        "    ║                                                 "
        "                               ║\n"
        f"    ║{Color.white}"
        "                         Created by brouane / bmarbouh"
        f"                          {Color.cyan}{Color.dim}║\n"
        "    ╠══════════════════════════════════════════════════"
        "══════════════════════════════╣\n"
        "    ║                                                  "
        "                              ║\n"
        f"    ║{Color.green}"
        "   ● Generate perfect & imperfect mazes               "
        f"                          {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.green}"
        "   ● Visualize solving algorithms                      "
        f"                         {Color.cyan}{Color.dim}║\n"
        f"    ║{Color.green}"
        "   ● Optional colored rendering                        "
        f"                         {Color.cyan}{Color.dim}║\n"
        "    ║                                                  "
        "                              ║\n"
        "    ╚══════════════════════════════════════════════════"
        "══════════════════════════════╝\n"
        f"    {Color.reset}"
    )
