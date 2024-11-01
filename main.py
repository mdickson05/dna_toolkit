# Testing DNA Toolkit
from sequences import sequence
from utilities import read_FASTA, readTextFile, writeTextFile

# Invalid string
# test_string = "XXAX"
# seq = sequence(string=test_string)

# Valid string but not all uppercase
# test_string = "TgaC"
# seq = sequence(string=test_string)

# Valid (default) string
seq = sequence()

# Generate random DNA string
# seq.generate()

# Generate random RNA string
seq.generate(type="RNA")
# Print info for sequence
seq.print_info()

# # Read FASTA files
# fasta_sequences = read_FASTA("fasta.txt")
# for s in fasta_sequences:
#     new_seq = sequence(label = s, string=fasta_sequences[s])
#     new_seq.print_info()


# # Write text file with current info
# writeTextFile("test.txt", f"{seq.type},{seq.seq},{seq.label}")

# # Read text file with generated sequence info
# file_input = readTextFile("test.txt")

# # Split input based on commas
# new_info = file_input.split(",")
# new_seq = sequence(type=new_info[0], string=new_info[1], label=new_info[2])

# print("\nImported sequence:")
# for rf in new_seq.generate_reading_frames(new_seq.seq):
#     print(rf)