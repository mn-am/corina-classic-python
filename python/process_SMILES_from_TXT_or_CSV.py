# This scripts reads SMILES from plain text file with one SMILES per line
# or SMILES in a CSV format, concatenates the SMILES records to a list that is
# handed over to CorinaBuffer to be processed
#
# pros:
# - the built-in CORINA Classic record statistics shows data of entirely
# processed file
#
# cons:
# - processing millions of SMILES this way is RAM intensive (about 25 mio
# compounds require about 5 GByte)
# - once the conversion to 3D started the python script cannot be interrupted
# by pressing Ctrl-C anymore


import os
import csv
import corina

# Configuration Constants
USE_PUBCHEM = True
WRITE_OUTPUT = True

# Configure source and target based on the flag
if USE_PUBCHEM:
    CONFIG = {
        "input_file": "CID-SMILES",
        "download_url": "https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz",
        "output_file": "CID-SMILES_3d.sdf",
        "smiles_column": 1,
        "max_records": 1000,
    }
else:
    CONFIG = {
        "input_file": "./GDB17.50000000LLnoSR.smi",
        "download_url": "https://zenodo.org/record/5172018/files/GDB17.50000000LLnoSR.smi.gz?download=1",
        "output_file": "./GDB17.50000000LLnoSR_3d.sdf",
        "smiles_column": 0,
        "max_records": 10000,
    }

# Check if the input file exists
if not os.path.isfile(CONFIG['input_file']):
    print(f"Seems that input file is missing, download it from {CONFIG['download_url']}")
    exit(1)

# Initialize output file
output_file = None
if WRITE_OUTPUT:
    output_file = open(CONFIG['output_file'], "w")

# Read SMILES from input file
all_smiles = []
with open(CONFIG['input_file']) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")
    for line_count, row in enumerate(csv_reader):
        if line_count >= CONFIG['max_records']:
            break
        smiles = row[CONFIG['smiles_column']].strip()
        all_smiles.append(smiles)

print("Finished reading SMILES. Starting 3D coordinate generation.")

# Generate 3D coordinates using Corina
corina_buffer = corina.CorinaBuffer()
corina_buffer.command = "corina -d wh -i t=smiles -o t=sdf"
corina_buffer.input = "\n".join(all_smiles)
if corina_buffer.proceed() and WRITE_OUTPUT:
    output_file.write(corina_buffer.output)

# Close output file
if WRITE_OUTPUT:
    output_file.close()

# Show statistics
print(f"Processed {line_count} of {CONFIG['max_records']}")
print("CORINA Classic record statistics:")
print(f"Number of records read: {corina_buffer.statsRead}")
print(f"Number of records converted: {corina_buffer.statsConverted}")
print(f"Number of records discarded: {corina_buffer.statsDiscarded}")
print(f"Number of CORINA Classic errors: {corina_buffer.statsErrors}")
