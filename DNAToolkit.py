# DNA Toolkit file
from constants import *

# Function to print information for a given DNA sequence
def print_information(seq):
    """Prints all information for an imported sequence"""
    print("Sequence: " + seq)
    isValid = validate_sequence(seq)
    print(f'[1] Is valid: {isValid}')
    if isValid:
        print(f"[2] Length: {len(seq)}")
        print(f"[3] Nucleotide Frequencies: {count_nuc(seq)}")
        print(f"[4] DNA -> RNA Transcription: {transcript_sequence(seq)}")
        
        # [5] was pretty much copied from this commit as it was awesome
        # https://gitlab.com/RebelCoder/dna-toolset/-/commit/8a4be0e3a70733be9bebdf0d9eed987c0fb44429
        
        print("[5] Reverse Complement:\n")
        print(f"5' {(seq)} 3'")
        print(f"   {''.join(['|' for c in range(len(seq))])}")
        print(f"3' {reverse_complement(seq)} 5'\n")


# Simple check whether sequence is valid DNA string
def validate_sequence(seq):
    """Simple check to see whether the imported DNA string is valid"""
    # Ensure imported sequence is uppercase
    to_check = seq.upper()
    for nuc in to_check:
        if nuc not in nucleotides:
            return False
    return True

# Function should return the frequency of each nucleotide
def count_nuc(seq):
    """Counts the nucleotide frequency within an imported DNA sequence"""
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
# TLDR: Replaces Thyamine with Uracil
def transcript_sequence(seq):
    """Transcripts an imported DNA sequence into its RNA counterpart"""
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
    """Finds the reverse complement of an imported DNA sequence"""
    if validate_sequence(seq):
        complement = ''
        for nuc in seq:
            # Find the complement for the nucleotide, add it to the string
            complement += nuc_complements[nuc]
        return complement[::-1] # ::-1 to reverse (Python magic!)
    else:
        print("Error: Invalid sequence - cannot reverse complement!")