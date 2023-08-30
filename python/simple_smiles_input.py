"""

Very simple example that takes a SMILES as input and output a SDF

"""
import corina

buffer = corina.CorinaBuffer()

smiles = "CCCCCC"

buffer.command = "corina -i t=smiles"  # specify the input file format
buffer.input = smiles

buffer.proceed()


# print output
print(buffer.output)

# print corina trace
print(buffer.log)
