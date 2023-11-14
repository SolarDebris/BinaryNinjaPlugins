from binaryninja import *
import binaryninja.mediumlevelil as mlil


def get_var_value(var, addr):

    variables = []
    variables.insert(0,var.name)

    # Will go through instructions in reverse starting from address
    for instr in reversed(list(current_function.mlil_instructions)):
        if instr.address > addr:
            continue
        # Pushes variables onto a stack until a constant is reached 
        if type(instr) == mlil.MediumLevelILSetVar:
            value = instr.operands[1]
            setvar = instr.operands[0]
            if variables[0] == setvar.name:
                if type(value) == mlil.MediumLevelILConst:
                    return value.constant
                elif type(value) == mlil.MediumLevelILZx or type(value) == mlil.MediumLevelILSx:
                    variables.insert(0,value.operands[0].var.name)
                elif type(value) == mlil.MediumLevelILVar:
                    variables.insert(0,value.var.name)
                elif type(value) == mlil.MediumLevelILLowPart:
                    variables.insert(0,value.operands[0].var.name)
        elif type(instr) == mlil.MediumLevelILSetVarSplit:
            if instr.operands[0].name == variables[0] or instr.operands[1].name == variables[0]:
                variables.insert(0,instr.operands[2].operands[0].var.name)
