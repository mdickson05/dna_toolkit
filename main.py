# Testing DNA Toolkit
from DNAToolkit import *
import random

# Generate random valid dna_string
input = ''.join([random.choice(nucleotides) for nuc in range(20)])

# Always valid + uppercase
dna_string = input.upper()

# Valid but not uppercase
# dna_string = "AgTcAAc"

# Invalid
# dna_string = "Hello, world!"

print_information(dna_string)

