# This scripts reads SMILES from plain text file with one SMILES per line
# or SMILES in a CSV format, concatenates the SMILES records to a list that is
# handed over to CorinaBuffer to be processed
#
# The input data is processed by chunks to decrease memory usage.


import os
import csv
import time

import corina

# Configuration Constants
USE_PUBCHEM = True
WRITE_OUTPUT = True
CHUNK_SIZE = 100


class CorinaStats:
    read: int
    converted: int
    discarded: int
    errors: int

    start_time: float  # in seconds
    end_time: float  # in seconds

    def __init__(self):
        self.read = 0
        self.converted = 0
        self.discarded = 0
        self.errors = 0
        self.start_time = time.time()
        self.end_time = None

    def add_stats_from_corina_buffer(self, buffer):
        self.read += buffer.statsRead
        self.converted += buffer.statsConverted
        self.discarded += buffer.statsDiscarded
        self.errors += buffer.statsErrors

    def stop(self):
        self.end_time = time.time()

    def get_computation_time(self) -> float:
        """Returns the computation time in seconds"""

        return self.end_time - self.start_time


# Configure source and target based on the flag
if USE_PUBCHEM:
    CONFIG = {
        "input_file": "CID-SMILES",
        "download_url": "https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz",
        "output_file": "CID-SMILES_3d.sdf",
        "smiles_column": 1,
        "max_records": 10000,
    }
else:
    CONFIG = {
        "input_file": "./GDB17.50000000LLnoSR.smi",
        "download_url": "https://zenodo.org/record/5172018/files/GDB17.50000000LLnoSR.smi.gz?download=1",
        "output_file": "./GDB17.50000000LLnoSR_3d.sdf",
        "smiles_column": 0,
        "max_records": 100000,
    }

# Check if the input file exists
if not os.path.isfile(CONFIG['input_file']):
    print(f"Seems that input file is missing, download it from {CONFIG['download_url']}")
    exit(1)

# Initialize output file
output_file = None
if WRITE_OUTPUT:
    output_file = open(CONFIG['output_file'], "w")

# initialize the statistics
corina_stats: CorinaStats = CorinaStats()

# Read SMILES from input file

with open(CONFIG['input_file']) as csv_file:
    all_smiles = []
    corina_buffer = corina.CorinaBuffer()
    corina_buffer.command = "corina -d wh -i t=smiles -o t=sdf"

    csv_reader = csv.reader(csv_file, delimiter="\t")
    for line_count, row in enumerate(csv_reader, start=1):
        if line_count > CONFIG['max_records']:
            break
        smiles = row[CONFIG['smiles_column']].strip()
        all_smiles.append(smiles)

        if line_count % CHUNK_SIZE == 0:
            corina_buffer.input = "\n".join(all_smiles)
            all_smiles = []

            # Generate 3D coordinates using Corina
            if corina_buffer.proceed():
                if WRITE_OUTPUT:
                    output_file.write(corina_buffer.output)

            # accumulate statistics
            corina_stats.add_stats_from_corina_buffer(corina_buffer)

corina_stats.stop()

# Close output file
if WRITE_OUTPUT:
    output_file.close()

# Show statistics
print(f"Processed {line_count} of {CONFIG['max_records']}")
print("CORINA Classic record statistics:")
print(f"Number of records read: {corina_stats.read}")
print(f"Number of records converted: {corina_stats.converted}")
print(f"Number of records discarded: {corina_stats.discarded}")
print(f"Number of CORINA Classic errors: {corina_stats.errors}")
print(f"Computation time: {corina_stats.get_computation_time()} seconds")
