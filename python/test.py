# define two "hardcoded" SD records

sd_records = """Benzene


  6  6  0  0  0  0  0  0  0  0999 V2000
    2.4249    0.7000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.4249    2.1000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2124    2.8000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    2.1000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    0.7000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2124    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  2  3  2  0  0  0  0
  3  4  1  0  0  0  0
  4  5  2  0  0  0  0
  5  6  1  0  0  0  0
  6  1  2  0  0  0  0
M  END
$$$$
Phenol


  7  7  0  0  0  0  0  0  0  0999 V2000
    2.4249    0.7000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.4249    2.1000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2124    2.8000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    2.1000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    0.7000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2124    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.6373    2.8000    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  2  3  2  0  0  0  0
  3  4  1  0  0  0  0
  4  5  2  0  0  0  0
  5  6  1  0  0  0  0
  6  1  2  0  0  0  0
  2  7  1  0  0  0  0
M  END
$$$$
"""

# import the Python module of CORINA Classic
import corina

# Create an instance of corinaBuffer
buffer = corina.CorinaBuffer()


# specify the input
buffer.input = sd_records

# specify run options in the command
buffer.command = "corina -o t=sdf3 -d wh" # options: output file format ic SD V3000 format

# do the 3D computation
buffer.proceed()

# print generated 3D structure in SD V3000 format
print(buffer.output)

# print CORINA Classic trace information
print(buffer.log)


print("CORINA Classic record statistics:")

print(f"Number of records read: {buffer.statsRead}")
print(f"Number of records converted: {buffer.statsConverted}")
print(f"Number of records discarded: {buffer.statsDiscarded}")
print(f"Number of CORINA Classic errors: {buffer.statsErrors}")
