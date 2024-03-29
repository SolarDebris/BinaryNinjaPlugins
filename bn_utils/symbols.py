from binaryninja import *
from binaryninjaui import *


def import_symbols(bv):
    """
    Imports function symbols and data variables from a file in the format 

    address func_name
    address func_name_2

    """

    import_prompt = interaction.OpenFileNameField("Select file to restore symbols from:") 

    symbols = open(import_prompt).read()



    for line in symbols.split("\n"):
        if len(line) == 2:
            addr, string = line
            if "0x" in addr:
                addr = int(addr,16)
            else:
                addr = int(addr,10)

            # !TODO add importing data symbols and other things as well
            func = bv.get_function_at(addr)
            if func != None:
                func.name = string



def export_symbols(bv):
    """
    Export function and data variables into a file

    """
    
    output = ""
    
    save_prompt = interaction.SaveFileNameField("Save to file").result
 

    for func in bv.functions:
        if "sub" not in func.name:
            output += hex(func.start) + " " + func.name + "\n"


    
