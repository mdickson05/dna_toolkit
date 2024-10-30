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

isValid = validate_sequence(dna_string)

print("DNA string '" + dna_string + "' is valid: " + str(isValid))
if isValid:
    count = count_nuc(dna_string)
    print("Count: " + str(count))
