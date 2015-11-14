# import theFunctions
from theFunctions import *

print "theMain module top  level - Hello"


def main():
    print "main() top level - Hello"
    print "main().{}".format(say_hi())
    print "main().", say_hello()
    print say_hey()


if __name__ == "__main__":
    main()
