# DNA Toolkit file

# List of nucleotides
# Adenine Guanine Thymine and Cytosine
nucleotides = ["A", "G", "T", "C"]

# Simple check whether sequence is valid DNA string
def validate_sequence(dna_seq):
    # Ensure imported sequence is uppercase
    to_check = dna_seq.upper()
    for nuc in to_check:
        if nuc not in nucleotides:
            return False
    return True

# Function should return the frequency of each nucleotide
def count_nuc(dna_seq):
    # First validates sequence
    if (validate_sequence(dna_seq)):
        freq_dict = {"A" : 0, "G" : 0, "T" : 0, "C" : 0}
        # Ensures dna_seq that is checked is in uppercase form
        to_check = dna_seq.upper()
        # For each nucleotide, add to dict where key = nuc
        for nuc in to_check:
            freq_dict[nuc] += 1
        return freq_dict
    # If the sequence is invalid...
    else:
        print("Error: Invalid sequence - cannot count!")