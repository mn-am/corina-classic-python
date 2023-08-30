"""
This example shows all functionalities of the API
"""

import corina

print("Is license valid?", corina.is_corina_license_valid())

# Create an instance of CorinaBuffer
buffer = corina.CorinaBuffer()

# show corina version
buffer.command = "corina -v"
buffer.proceed()

# show corina help
buffer.command = "corina -h"
buffer.proceed()

# show corina help for the driver subcommand
buffer.command = "corina -h d"
buffer.proceed()

smiles = "CCCCCC"

buffer.command = "corina -i t=smiles -o t=sdf3"
buffer.input = smiles

success = buffer.proceed() # proceed() returns True or False
status = buffer.status # exit code status of the corina process, if  it is 0 it worked OK




# print output
print(buffer.output)

# print corina trace
print(buffer.log)

print(f"success: {success}    CORINA exit code status: {status}")

print("\nCORINA record statistics:")
print(f"Number of compounds read: {buffer.statsRead}")
print(f"Number of compounds converted: {buffer.statsConverted}")
print(f"Number of compounds discarded: {buffer.statsDiscarded}")
print(f"Number of CORINA errors: {buffer.statsErrors}")
