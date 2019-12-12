colors = {
    'DANGER': '\033[91m',
    'WARNING': '\033[33m',
    'MILD': '\033[94m',
    'OK': '\033[92m',
    'RESET': '\033[0m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
}


def color(text, text_color):
    if text_color in colors:
        return ''.join([colors[text_color], text, colors['RESET']])
    return text