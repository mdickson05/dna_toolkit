# Testing DNA Toolkit
from DNAToolkit import *
from sequences import sequence




# Always valid + uppercase
# dna_string = input.upper()

# Valid but not uppercase
# dna_string = "AgTcAAc"

# Invalid
# dna_string = "Hello, world!"

# Create new default sequence
seq = sequence()
# Generate random values
seq.generate()
# Print info for sequence
seq.print_info()

