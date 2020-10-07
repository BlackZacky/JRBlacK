class terminal:
    terminal_bright = "\x1b[1m"
    terminal_dim = "\x1b[2m"
    terminal_underscore = "\x1b[4m"
    terminal_blink = "\x1b[5m"
    terminal_reverse = "\x1b[7m"
    terminal_hidden = "\x1b[8m"

    terminal_foreground_black = "\x1b[30m"
    terminal_foreground_red = "\x1b[31m"
    terminal_foreground_green = "\x1b[32m"
    terminal_foreground_yellow = "\x1b[33m"
    terminal_foreground_blue = "\x1b[34m"
    terminal_foreground_magenta = "\x1b[35m"
    terminal_foreground_cyan = "\x1b[36m"
    terminal_foreground_white = "\x1b[37m"

    terminal_background_black = "\x1b[40m"
    terminal_background_red = "\x1b[41m"
    terminal_background_green = "\x1b[42m"
    terminal_background_yellow = "\x1b[43m"
    terminal_background_blue = "\x1b[44m"
    terminal_background_magenta = "\x1b[45m"
    terminal_background_cyan = "\x1b[46m"
    terminal_background_white = "\x1b[47m"

class common:
    hexa_foreground_black = "aaaa"
    hexa_foreground_red = "aaa"
    hexa_foreground_green = "aaaa"
    hexa_foreground_yellow = "12"

class colors(terminal, common):
    pass