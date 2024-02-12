"""
This plugin is for patching out specific things from binaries.
"""
from binaryninja import *


def remove_fork():
    """
    Patches out any fork syscalls from the binary.
    """
    return None

def remove_ptrace():
    """
    Patches out all ptrace calls from the binary that 
    check for debuggers. 
    """
    return None

def remove_sleep():
    """
    Patches out sleep function calls from the binary.
    """
    return None


PluginCommand.register("Remove ptrace anti-debugging", remove_ptrace)
PluginCommand.register("Remove fork syscalls", remove_fork)
