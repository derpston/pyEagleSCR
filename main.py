import sys
import re
import models

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

# TODO What's the Eagle default for layer and grid?
# Any other default settings?

context = {
        'layer': 0
    ,   'grid': None 
    ,   'symbols': {}
    ,   'devices': {}
    ,   'packages': {}
    ,   'settings': {}
    }

current_obj = None

for line in open(sys.argv[1]):
    line = line.strip()

    if len(line) == 0 or line.startswith("#"):
        continue # Skip empty lines and commands.

    # Ask each model if it matches the line we're considering. If it does, it
    # will return an instance of itself.
    for model in models_to_match:
        match = re.compile(model.regex).match(line)
        if match:
            obj = model(context, **match.groupdict())
            break
        else:
            obj = None

    if not obj:
        # No class wanted to claim a match for this line, so skip it.
        print "Unsupported command: %s" % (line)
        continue
    
    # These commands set up a new Symbol, Device or Package.
    if isinstance(obj, models.EditSymbol):
        context['symbols'][obj.name] = obj
        current_obj = obj
    elif isinstance(obj, models.EditDevice):
        context['devices'][obj.name] = obj
        current_obj = obj
    elif isinstance(obj, models.EditPackage):
        context['packages'][obj.name] = obj
        current_obj = obj

    # These commands modify the global context, so we can just handle them
    # here.
    elif isinstance(obj, models.Layer):
        context['layer'] = obj.num
    elif isinstance(obj, models.Grid):
        context['grid'] = obj.value
    elif isinstance(obj, models.Set):
        context['settings'][obj.key] = obj.value

    elif current_obj is not None:
        # This is a command inside a large block like a Package, Symbol or
        # Device, so that model should be able to handle this.
        current_obj.handle(obj)
    else:
        print "Unsupported command: %s" % (obj)

print "Context:"
import pprint
pprint.pprint(context)

