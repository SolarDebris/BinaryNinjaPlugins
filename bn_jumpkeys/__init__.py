"""
This plugin is meant to add more keybindings for moving around in binja
that I use. 
"""
from binaryninja import *
from binaryninjaui import *

from PySide6.QtGui import QKeySequence


def jump_end_of_block(bv, addr):
    """
    Jump to the end of a basic block.
    """
    blocks = bv.get_basic_blocks_at(addr)

    if len(blocks) <= 0:
        return None

    start_block = blocks[0]
    bv.navigate(bv.view, start_block.end - 1)

    return None

def jump_start_of_block(bv, addr):
    """
    Jump to the start of a basic block.
    """
    blocks = bv.get_basic_blocks_at(addr)

    if len(blocks) <= 0:
        return None

    start_block = blocks[0]
    bv.navigate(bv.view, start_block.start)

    return None

def jump_down_left_block(bv, addr):
    """
    Jump to the next block if there is a conditional 
    branch go to the left block.
    """
    blocks = bv.get_basic_blocks_at(addr)

    if len(blocks) <= 0:
        return None

    start_block = blocks[0]

    if len(start_block.outgoing_edges) <= 0:
        return None

    target_block = start_block.outgoing_edges[0].target
    bv.navigate(bv.view, target_block.start)

    return None

def jump_down_right_block(bv, addr):
    """
    Jump to the next block. If there is a conditional
    branch go to the right block.
    """
    blocks = bv.get_basic_blocks_at(addr)

    if len(blocks) <= 0:
        return None

    start_block = blocks[0]

    if len(start_block.outgoing_edges) <= 0:
        return None

    target_block = start_block.outgoing_edges[-1].target
    bv.navigate(bv.view, target_block.start)

    return None

def jump_right_block(bv, addr):
    """
    Move to the right block in control flow graph view 
    """


def jump_up_block(bv, addr):
    """
    Jump to the basic block above.
    """
    blocks = bv.get_basic_blocks_at(addr)

    if len(blocks) <= 0:
        return None

    start_block = blocks[0]

    target_block = start_block.source_block

    if target_block is None:
        return None

    bv.navigate(bv.view, target_block.start)
    
    return None


PluginCommand.register_for_address("Binja Jumpkeys\Jump to start of block", "Moves cursor to the start of the current basic block", jump_start_of_block)
PluginCommand.register_for_address("Binja Jumpkeys\Jump to end of block", "Moves cursor to the end of the current basic block", jump_end_of_block)
PluginCommand.register_for_address("Binja Jumpkeys\Jump to next true block", "Moves cursor to the next leftmost basic block", jump_down_left_block)
PluginCommand.register_for_address("Binja Jumpkeys\Jump to next false block", "Moves cursor to the next rightmost basic block", jump_down_right_block)
#PluginCommand.register_for_address("Binja Jumpkeys\Jump to left block", "Moves cursor to the left block from the current basic block", jump_left_block)
#PluginCommand.register_for_address("Binja Jumpkeys\Jump to right block", "Moves cursor to the right block from the current basic block", jump_right_block)
PluginCommand.register_for_address("Binja Jumpkeys\Jump to up block", "Moves cursor to the last block from the current basic block", jump_up_block)

