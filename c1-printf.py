# Using ctype Library and other Dynamic libraries
from ctypes import *

msvcrt = CDLL('msvcrt')
message_string = b"Hola Mundo! DooVsDoo\n"
msvcrt.printf(b"Testing: %s", message_string)