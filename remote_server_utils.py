import sys


def check_on_hogwarts():
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        return True
    else:
        return False
