# From http://code.activestate.com/recipes/134892/

# implements unbuffered character reading from stdin
# works on both Windows and Unix

class _Get_Char:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _Get_Char_Windows()
        except ImportError:
            self.impl = _Get_Char_Unix()

    def __call__(self): return self.impl()


class _Get_Char_Unix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _Get_Char_Windows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


get_char = _Get_Char()

