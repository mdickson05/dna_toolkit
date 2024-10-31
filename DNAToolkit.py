# DNA Toolkit file
from collections import Counter
from constants import *
from utilities import coloured

# Function to print information for a given DNA sequence
def print_information(input):
    """Prints all information for an imported sequence"""
    print("Sequence: " + coloured(input))
    isValid = validate_sequence(input)
    print(f'[1] Is valid: {isValid}')
    if isValid:
        seq = input.upper()
        print(f"[2] Length: {len(seq)}")
        print(coloured(f"[3] Nucleotide Frequencies: {count_nuc(seq)})"))
        print(f"[4] DNA -> RNA Transcription: {coloured(transcript_sequence(seq))}")
        
        # [5] was pretty much copied from this commit as it was awesome
        # https://gitlab.com/RebelCoder/dna-toolset/-/commit/8a4be0e3a70733be9bebdf0d9eed987c0fb44429
        
        print("[5] Reverse Complement:\n")
        print(f"5' {coloured(seq)} 3'")
        print(f"   {''.join(['|' for c in range(len(seq))])}")
        print(f"3' {coloured(complement(seq))} 5' [Complement]")
        print(f"5' {coloured(reverse_complement(seq))} 3' [Reverse Complement]\n")
        print(f"[6] GC Content: {gc_content(seq)}%")
        print(f"[7] GC Content of subsequences (window size = 5): {gc_content_subseq(seq, 5)}")
        print(f"[8] Amino Acids Sequence from DNA sequence: {translate_seq(seq, 0)}")
        print(f"[9] Codon frequency (L): {codon_frequency(seq, "L")}")
        print("[10] Reading frames:")
        rf = generate_reading_frames(seq)

        for frame in rf:
            print(frame)
        print("[11] Protein analysis:")
        for frame in rf:
            print(find_rf_proteins(frame))
        
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

# Complement finder - Find complement string via nuc_complements
def complement(seq):
    """Finds the reverse complement of an imported DNA sequence"""
    if validate_sequence(seq):
        complement = ''
        for nuc in seq:
            # Find the complement for the nucleotide, add it to the string
            # Ensures uppercase lettering
            complement += nuc_complements[nuc.upper()]
        return complement
    else:
        print("Error: Invalid sequence - cannot find complement!")

# Reverse complement - calls complement, reverses + returns output
def reverse_complement(seq):
    return complement(seq)[::-1]

# Simple function to return GC content of an DNA sequence
def gc_content(seq):
    """Function to return GC content of an imported DNA sequence"""
    return round(((seq.count("G") + seq.count("C")) / len(seq)) * 100)

# Function that calculates the GC content for a specific window of nucleotides
# i.e. if len(seq) = 20, and k = 5, will find GC content for 1-5, 6-10, etc.
def gc_content_subseq(seq, window_size):
    """Given imported window size, find the GC content of each subsequence within 
    each window for an imported DNA sequence"""
    res = []
    # for i in range 0 to len(seq) - window_size + 1
    # Each iteration, i increases by window_size
    for i in range(0, len(seq) - window_size + 1, window_size):
        # subseq is between current i value and i + window_size
        subseq = seq[i : i + window_size]
        res.append(gc_content(subseq))
    return res

# Function that translates imported DNA sequence to amino acid codons
def translate_seq(seq, init_pos):
    """Imports a DNA sequence and a starting position to translate a DNA string into amino acid codons"""
    codons = []
    # Starts at init_pos, finishes at len(seq) - 2 (to avoid reading past the last triplet), increments by 3.
    for pos in range(init_pos, len(seq) - 2, 3):
        codons.append(dna_codons[seq[pos:pos+3]])
    return codons

# Function that returns a frequency map of an imported amino acid within a DNA sequence
def codon_frequency(seq, amino_acid):
    """Returns a frequency map of an imported amino acid within an imported DNA sequence"""
    temp_list = []
   # Starts at init_pos, finishes at len(seq) - 2 (to avoid reading past the last triplet), increments by 3.
    for i in range(0, len(seq) - 2, 3):
        # Sequence to check is between i and i + 3
        to_check = seq[i:i+3]
        # If the codon value of to_check chars matches the imported amino_acid
        if dna_codons[to_check] is amino_acid:
            # add to temporary list
            temp_list.append(to_check)

    # Defines a dictionary where the keys are the values in temp_list
    # And the values are their count within that list
    frequency_map = dict(Counter(temp_list))
    total_weight = sum(frequency_map.values())
    for seq in frequency_map:
        # Replaces the total count with their relative frequency within the list
        # E.g. if CTG appears twice, and CTC appears once - CTG: 0.67, CTC: 0.33 
        # 2 at the end is to signify rounding to 2dp
        frequency_map[seq] = round(frequency_map[seq] / total_weight, 2)
    return frequency_map

# Function to generate reading frames for imported sequence
def generate_reading_frames(seq):
    """Generates reading frames for imported sequence"""
    frames = []
    # Frames starting from each possible init_pos (without excluding data)
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    # Reverse complement frames
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))

    return frames

# Function that finds the list of proteins within an amino acid sequence
def find_rf_proteins(aa_seq):
    """Find a list of proteins within an amino acid sequence """
    current_prot = []
    proteins = []

    # For each amino acid in sequence
    for aa in aa_seq:
        # If aa is stop protein
        if aa == "_":
            # if current_prot exists...
            # i.e. an entry exists in the current_prot list
            if current_prot:
                # For each protein in current_prot
                for p in current_prot:
                    # Append to proteins list
                    proteins.append(p)
                # clear current_prot
                current_prot = []
        else:
            # If aa is start
            if aa == "M":
                # Append first protein to list
                current_prot.append("")
        
            # For loop is necessary in case of multiple overlapping sequences
            # i.e. MAAMC: current_prot = ["AAC", "C"]
            for i in range(len(current_prot)):
                current_prot[i] += aa

    return proteins
