import sys
import re
import models
import parser

# TODO Support more Eagle SCR commands
# Unsupported:
# Change (applies to Package and Symbol)
# Text (applies to Package and Symbol)
# Value (applies to Device?)
# Pad (through hole components, applies to Package?)
# Technology (applies to Device?)
# Wire (four-tuple variant, probably for rectangles?)

# TODO Support stripping comments after the end of a command.
# More examples in https://github.com/sparkfun/SparkFun_Eagle_Settings/blob/master/scr/eagle.scr

models_to_match = [
        models.Prefix
    ,   models.EditDevice
    ,   models.EditSymbol
    ,   models.Pin
    ,   models.Wire
    ,   models.Layer
    ,   models.Connect
    ,   models.Description
    ,   models.Attribute
    ,   models.EditPackage
    ,   models.Package
    ,   models.Add
    ,   models.Package
    ,   models.Smd
    ,   models.Grid
    ,   models.Set
    ]

parser = parser.Parser()

for line in open(sys.argv[1]):
    parser.handle_line(line)

print "Context:"
import pprint
pprint.pprint(parser.context)

