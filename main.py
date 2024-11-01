# Testing DNA Toolkit
from sequences import sequence

# Invalid string
# test_string = "XXAX"
# seq = sequence(string=test_string)
# Valid but not all uppercase
# test_string = "TgaC"
# seq = sequence(string=test_string)

# Valid/Default
seq = sequence()
# Generate random DNA string
# seq.generate()
# Generate random RNA string
seq.generate(type="RNA")
# Print info for sequence
seq.print_info()

