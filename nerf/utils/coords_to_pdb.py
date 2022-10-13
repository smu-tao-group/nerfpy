#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Save coordinates to PDB file
"""


def coords_to_pdb(pdb_dir, coords, new_pdb_dir):
    """Save coordinates to PDB file

    Args:
        pdb_dir (str): path to PDB file
        coords (list): 2D coordinates
        new_pdb_dir (str): path to new PDB file
    """
    pdb = open(pdb_dir, "r").readlines()
    idx = 0
    new_lines = []

    for line in pdb:
        if line[:4] != "ATOM":
            new_lines.append(line)
            continue

        new_line = line[:30]
        for i in range(3):
            new_line += str(round(coords[idx][i], 3)).rjust(8, " ")
        new_line += line[54:]
        new_lines.append(new_line)
        idx += 1

    assert idx == len(coords), "inconsistent coordinate and PDB size"

    # write to new file
    new_file = open(new_pdb_dir, "w")
    for line in new_lines:
        new_file.write(line)
    new_file.close()
