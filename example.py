import sys
sys.path.append("eaglescr")
import parser
import pprint
import argparse

argparser = argparse.ArgumentParser(description="Parse an Eagle SCR file and "\
    "display some basic information about it.")
argparser.add_argument('path', metavar='path-to-scr-file', type=str, \
    help="Path to an Eagle SCR file.")
args = argparser.parse_args()

# Eagle SCR parser.
scrparser = parser.Parser()

for line_index, line in enumerate(open(args.path)):
    if not scrparser.handle_line(line):
        print "Unsupported command on line %d: %s" % (line_index, repr(line))

print "Context:"
pprint.pprint(scrparser.context)

