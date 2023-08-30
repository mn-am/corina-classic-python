"""
Converting a 2D SD file into a 3D SD file
An SD file should be converted into 3D. Implicit hydrogen atoms should be added,
small fragments (e.g., counter ions in salts) should be removed and all molecules
should be neutralized.  The output file
should also be formatted in SD file format.
"""

import corina

mol_data = None
with open("use_case1.sdf") as f:
    mol_data = f.read()

    assert mol_data

    # Create an instance of CorinaBuffer
    buffer = corina.CorinaBuffer()

    buffer.command = "corina -d wh,rs,neu,r2d"

    buffer.input = mol_data
    buffer.proceed()

    print(buffer.output)
