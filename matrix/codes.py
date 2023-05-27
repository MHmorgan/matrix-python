"""ANSI escape codes for terminal control and coloring"""

BEL = "\a"
BACKSPACE = "\b"
HORIZONTAL_TAB = "\t"
LINE_FEED = "\n"
VERTICAL_TAB = "\v"
FORM_FEED = "\f"
CARRAGE_RETURN = "\r"
ESC = "\x1B"
DEL = "\x7F"

# Cursor handling
HIDE = ESC + "[?25l"
SHOW = ESC + "[?25h"
HOME = ESC + "[H"
SAVE = ESC + "7"  # Also save attributes
RESTORE = ESC + "8"

# Screen handling
SAVE_SCREEN = ESC + "[?47h"
RESTORE_SCREEN = ESC + "[?47l"
EN_ALT_SCREEN_BUF = ESC + "[?1049h"
DIS_ALT_SCREEN_BUF = ESC + "[?1049l"

# Clear line
CLEAR_END = ESC + "[0K"  # From cursor to end of line
CLEAR_BEGINNING = ESC + "[1K"  # From cursor to beginning of line
CLEAR_LINE = ESC + "[2K"
CLEAR_SCREEN = ESC + "[2J"

# Control text attributes
RESET = ESC + "[0m"
BOLD = ESC + "[1m"
DIM = ESC + "[2m"
ITALIC = ESC + "[3m"
UNDERSCORE = ESC + "[4m"
BLINK = ESC + "[5m"
INVERSE = ESC + "[7m"
HIDDEN = ESC + "[8m"
CROSSED_OUT = ESC + "[9m"
FRAKTUR = ESC + "[20m"
DOUBLE_UNDERSCORE = ESC + "[21m"
NO_BOLD = ESC + "[22m"
NO_ITALIC = ESC + "[23m"
NO_DOUBLE_UNDERSCORE = ESC + "[24m"
NO_BLINK = ESC + "[25m"
NO_INVERSE = ESC + "[27m"
REVEAL = ESC + "[28m"
NO_CROSSED_OUT = ESC + "[29m"
FRAMED = ESC + "[51m"
ENCIRCLED = ESC + "[53m"

# Control foreground coloring
FG_BLACK = ESC + "[30m"
FG_RED = ESC + "[31m"
FG_GREEN = ESC + "[32m"
FG_YELLOW = ESC + "[33m"
FG_BLUE = ESC + "[34m"
FG_MAGENTA = ESC + "[35m"
FG_CYAN = ESC + "[36m"
FG_WHITE = ESC + "[37m"
FG_DEFAULT = ESC + "[39m"
FG_BRIGHT_BLACK = ESC + "[90m"
FG_BRIGHT_RED = ESC + "[91m"
FG_BRIGHT_GREEN = ESC + "[92m"
FG_BRIGHT_YELLOW = ESC + "[93m"
FG_BRIGHT_BLUE = ESC + "[94m"
FG_BRIGHT_MAGENTA = ESC + "[95m"
FG_BRIGHT_CYAN = ESC + "[96m"
FG_BRIGHT_WHITE = ESC + "[97m"

# Control background coloring
BG_BLACK = ESC + "[40m"
BG_RED = ESC + "[41m"
BG_GREEN = ESC + "[42m"
BG_YELLOW = ESC + "[43m"
BG_BLUE = ESC + "[44m"
BG_MAGENTA = ESC + "[45m"
BG_CYAN = ESC + "[46m"
BG_WHITE = ESC + "[47m"
BG_DEFAULT = ESC + "[49m"
BG_BRIGHT_BLACK = ESC + "[100m"
BG_BRIGHT_RED = ESC + "[101m"
BG_BRIGHT_GREEN = ESC + "[102m"
BG_BRIGHT_YELLOW = ESC + "[103m"
BG_BRIGHT_BLUE = ESC + "[104m"
BG_BRIGHT_MAGENTA = ESC + "[105m"
BG_BRIGHT_CYAN = ESC + "[106m"
BG_BRIGHT_WHITE = ESC + "[107m"


# ------------------------------------------------------------------------------
# FUNCTIONS

# Cursor handling
def MOVE(ROW, COL):
    return f'{ESC}[{ROW};{COL}H'


def UP(N):
    return f'{ESC}[{N}A'


def DOWN(N):
    # ESC "[" #N "B"
    return f'{ESC}[{N}B'


def FORWARD(N):
    return f'{ESC}[{N}C'


def BACKWARD(N):
    # ESC "[" #N "D"
    return f'{ESC}[{N}D'


def NEXT_LINE(N):
    # ESC "[" #N "E"
    return f'{ESC}[{N}E'


def PREV_LINE(N):
    # ESC "[" #N "F"
    return f'{ESC}[{N}F'


def TO_COLUMN(N):
    # ESC "[" #N "G"
    return f'{ESC}[{N}G'


# Screen handling

def SCROLL_UP(N):
    # ESC "[" #N "S"
    return f'{ESC}[{N}S'


def SCROLL_DOWN(N):
    # ESC "[" #N "T"
    return f'{ESC}[{N}T'


# Control foreground coloring


def FG_RGB(R, G, B):
    # ESC "[38;2;" #R ";" #G ";" #B "m"
    return f'{ESC}[38;2;{R};{G};{B}m'


# The number N sets the color. The colors are:
# 0-black, 1-red, 2-green, 3-yellow, 4-blue, 5-magenta, 6-cyan, 7-white.
# 8-15: high intensity colors, the colors are in the same order as 0-7.
# 16-231: 6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
# 232-255:  grayscale from black to white in 24 steps
def FG_SET(N):
    # ESC "[38;5;" #N "m"
    return f'{ESC}[38;5;{N}m'


def BG_SET(N):
    # ESC "[48;5;" #N "m"
    return f'{ESC}[48;5;{N}m'


# Control background coloring


def BG_RGB(R, G, B):
    # ESC "[48;2;" #R ";" #G ";" #B "m"
    return f'{ESC}[48;2;{R};{G};{B}m'
