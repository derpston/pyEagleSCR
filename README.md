pyEagleSCR
--
pyEagleSCR is a pure Python parser for the scripting language used by [AutoDesk/CADSoft Eagle's PCB schematic/layout tool](https://www.autodesk.com/products/eagle).

For now, it aims to support only the functionality needed to parse symbols and packages, to ease use of part specifications in other tools like [KiCad](http://kicad-pcb.org/).

TODO
==

* Support more Eagle SCR commands, like:
  * Change (applies to Package and Symbol)
  * Text (applies to Package and Symbol)
  * Value (applies to Device?)
  * Pad (through hole components, applies to Package?)
  * Technology (applies to Device?)
  * Wire (four-tuple variant, probably for rectangles?)
* Support stripping comments after the end of a command.
  * More examples in https://github.com/sparkfun/SparkFun_Eagle_Settings/blob/master/scr/eagle.scr
* Set up sensible defaults in the context, to match what Eagle does.
  * layer
  * grid
  * Any other default settings that should be initialised here?
* Support case-insensitive commands
* Python 3 support
* Tests!
