#!/usr/bin/python3

import binaryninja as bn
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./analyze_binaries (list_of_binaries) (binary_database)")
        exit()

    binary_list = open(sys.argv[1]).read().split("\n")
    binary_database = sys.argv[2]
    for binary in binary_list:
        if os.path.exists(binary):
            bv = bn.open_view(binary)
            binary_name = bv.file.filename
            bv.save(f"{binary_database}/{binary_name}.bndb")
