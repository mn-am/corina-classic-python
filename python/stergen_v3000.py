"""

Stereo isomer generation.

The SD V3000 format offers some stereochemical extensions for asymmetric atoms
(tetrahedral chiral centers).

The V3000 stereochemical extensions are interpreted and processed by CORINA and
the stereoisomer generation module. The full consideration and interpretation of the
extensions is switched on by the additional option v3000.

Permute all stereocenters that belong to one of the
stereo-chemical groups "STERELn" and "STERACn"
according to their definition of their relative or racemic
representation, but do not permute stereocenters that
belong to the group "STERABS"

The example structure was found in the "BIOVIA ENHANCED STEREOCHEMICAL REPRESENTATION WHITE PAPER"
and is described in the CORINA manual (Figure 44).


"""
import corina

mol_data = None
with open("MDL_white_paper_fig22.v3000.sdf") as f:
    mol_data = f.read()

assert mol_data

# Create an instance of CorinaBuffer
buffer = corina.CorinaBuffer()

msc = 10  # maximum number of processed stereo centers (default is 4)
msi = 200  # maximum number of output stereoisomers

print("Without v3000 option")
buffer.command = f"corina  -o t=sdf2 -d stergen,msc={msc},msi={msi}"
buffer.input = mol_data
buffer.proceed()

print(f'Number of input compounds: {buffer.statsRead}')
print(f'Number of isomers generated: {buffer.statsWritten}')  # should be 128


print("With v3000 option")
buffer.command = f"corina  -o t=sdf2 -d stergen,v3000,msc={msc},msi={msi}"
buffer.input = mol_data
buffer.proceed()

print(f'Number of input compounds: {buffer.statsRead}')
print(f'Number of isomers generated: {buffer.statsWritten}')  # should be 16
