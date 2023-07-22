import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.ghostbusters("Dobranoc, " + sys.argv[1])