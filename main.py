import sys
import re
import models
import parser
import pprint

parser = parser.Parser()

for line_index, line in enumerate(open(sys.argv[1])):
    if not parser.handle_line(line):
        print "Unsupported command on line %d: %s" % (line_index, repr(line))

print "Context:"
pprint.pprint(parser.context)

