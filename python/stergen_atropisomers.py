"""
Stereo isomer generation.

Examples of atropisomer generation (example from the CORINA Classic user manual Figure 28)

"""

import corina

mol_data = "c2ccc1c5c(ccc1c2)OCCCCCCOc4ccc3ccccc3c45"

# Create an instance of CorinaBuffer
buffer = corina.CorinaBuffer()

msc = 10  # maximum number of processed stereo centers (default is 4)

print("Without axchir option")
buffer.command = f"corina  -i t=smiles -o t=sdf2 -d stergen,msc={msc}"
buffer.input = mol_data
buffer.proceed()

print(f'Number of input compounds: {buffer.statsRead}')
print(f'Number of isomers generated: {buffer.statsConverted}')  # should be 1

print("With axchir option")
buffer.command = f"corina  -i t=smiles -o t=sdf2 -d axchir,stergen,msc={msc}"  # the  axial chirality option "axchir" is required
buffer.input = mol_data
buffer.proceed()

print(f"Number of compounds read: {buffer.statsRead}")
print(f"Number of compounds converted: {buffer.statsConverted}")  # should be 2
