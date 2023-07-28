"""
A set of useful small plugins that I use. 
"""
from binaryninja import *
from sections import *


PluginCommand.register_for_address("Change section type", "Changes all data in a section to a specific type", make_section_type)
