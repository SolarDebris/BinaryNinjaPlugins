"""
This plugin deals with changing sections and doing 
operations based on them. 
"""

from binaryninja import *
from binaryninjaui import *

def make_section_type_address(bv, addr):
    """
    Prompt the user for a type in the binaryview and make everything
    that type in the section.
    """
    sections = bv.get_sections_at(addr)
    
    if len(sections) <= 0:
        return None

    section = sections[0]

    if section.semantics != SectionSemantics.ReadOnlyDataSectionSemantics:
        return None
    
    type_prompt = TextLineField("Enter type:")
    assert get_form_input(["Type Entire Section", type_prompt], "Type Entire Section")
    target_type = bv.parse_type_string(type_prompt.result)
   
    bv.begin_undo_actions()
    for address in range(section.start, section.end, 40):
        data_var = bv.get_data_var_at(address)
        string = type_prompt.result + "_" + hex(address).split("0x")[1]
        bv.define_data_var(address, target_type, string)

    bv.commit_undo_actions()
    return None


def make_section_type(bv):
    """
    Prompt the user for a type in the binaryview and make everything
    that type in the section.
    """
    
    type_prompt = TextLineField("Type:")
    section_prompt = TextLineField("Section:")
    assert get_form_input(["Type Entire Section", section_prompt, type_prompt], "Type Entire Section")

    target_type = bv.parse_type_string(type_prompt.result) 
    section = bv.get_section_by_name(section_prompt.result)
    
    if section.semantics != SectionSemantics.ReadOnlyDataSectionSemantics:
        return None

    bv.begin_undo_actions()
    for address in range(section.start, section.end, 40):
        data_var = bv.get_data_var_at(address)
        string = type_prompt.result + "_" + hex(address).split("0x")[1]
        bv.define_data_var(address, target_type, string)
    bv.commit_undo_actions()
    
    return None

def make_section_string(bv):
    """
    Changes all data vars in a section into c strings.
    """

    return None
