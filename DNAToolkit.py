# DNA Toolkit file
# Constants
# List of nucleotides: Adenine Guanine Thymine and Cytosine
nucleotides = ["A", "G", "T", "C"]
# Dictionary of complements: Maps each nucleotide to its complement
nuc_complements = {"A" : "T", "G" : "C", "T" : "A", "C" : "G"}

# Function to print information for a given DNA sequence
def print_information(seq):
    print("Sequence: " + seq)
    isValid = validate_sequence(seq)
    print(f'[1]  Is valid: {isValid}')
    if isValid:
        print(f'[2]  Length: {len(seq)}')
        print(f'[3]  Nucleotide Frequencies: {count_nuc(seq)}')
        print(f'[4]  DNA -> RNA Transcription: {transcript_sequence(seq)}')
        print(f'[5]  Reverse Complement: {reverse_complement(seq)}')


# Simple check whether sequence is valid DNA string
def validate_sequence(seq):
    # Ensure imported sequence is uppercase
    to_check = seq.upper()
    for nuc in to_check:
        if nuc not in nucleotides:
            return False
    return True

# Function should return the frequency of each nucleotide
def count_nuc(seq):
    # First validates sequence
    if (validate_sequence(seq)):
        freq_dict = {"A" : 0, "G" : 0, "T" : 0, "C" : 0}
        # Ensures dna_seq that is checked is in uppercase form
        to_check = seq.upper()
        # For each nucleotide, add to dict where key = nuc
        for nuc in to_check:
            freq_dict[nuc] += 1
        return freq_dict
    # If the sequence is invalid...
    else:
        print("Error: Invalid sequence - cannot count!")

# Simple function to transcript a DNA sequence into its RNA counterpart
# TLDR: DNA -> RNA transcription = replacing Thyamine with Uracil
def transcript_sequence(seq):
    if validate_sequence(seq):
        transcripted = seq.replace("T", "U")
        return transcripted
    else:
        print("Error: Invalid sequence - cannot transcript!")

# Reverse complement finder
# Steps:
# 1. Find complement string via nuc_complements
# 2. Reverse the complement string
def reverse_complement(seq):
    if validate_sequence(seq):
        complement = ''
        for nuc in seq:
            # Find the complement for the nucleotide, add it to the string
            complement += nuc_complements[nuc]
        return complement[::-1] # ::-1 to reverse (Python magic!)
    else:
        print("Error: Invalid sequence - cannot reverse complement!")