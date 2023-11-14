from binaryninja import *


def get_string_args_from_xrefs(bv, func):
    """
    This function will print all of the strings used in
    all calls to a specific function.
    """
    for refs in func.caller_sites:
        for param in refs.mlil.params:
            if param.type == binaryninja.mediumlevelil.MediumLevelILConstPtr:
                value = bv.get_data_var_at(param.constant))))
                if value.type == bv.types.CharType:
                    print(get_string_at(value)) 
                elif value.type.name == "CFString":
    return None

def get_number_of_callees(bv):
    return None

