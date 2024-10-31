from constants import * 
from utilities import coloured
import random

class sequence:
    """Class for sequences. Constructor imports sequence string, type, and label"""
    def __init__(self, string="ATGC", type="DNA", label="No label"):
        self.seq = string.upper()
        self.label = label
        self.type = type
        self.is_valid = self.__validate(self.seq)
        # Throws assertion error if is_valid is False
        assert self.is_valid, f"Provided sequence is invalid: {self.seq}"

    # Generate random valid sequence
    def generate(self, length=20, seq_type="DNA"):
        """Generate random valid sequence"""
        seq = ''.join([random.choice(nucleotides) for nuc in range(length)])
        self.__init__(seq, seq_type, "Randomly Generated Sequence")


    # Simple check whether sequence is valid DNA string
    def __validate(self, seq):
        """Simple check to see whether the imported DNA string is valid"""
        # Ensure imported sequence is uppercase
        to_check = seq.upper()
        for nuc in to_check:
            if nuc not in nucleotides:
                return False
        return True

    # Simple "to string" method for the sequence itself
    def __describe(self):
        """Returns basic sequence info"""
        return f"\t[Label] {self.label}\n\t[Sequence] {coloured(self.seq)}\n\t[Type] {self.type}\n\t[Is valid?] {self.is_valid}"


    def print_info(self):
        """Prints all available information for sequence"""
        
        print("[1] Sequence Information")
        print(self.__describe())

        print(f"[2] Length: {len(self.seq)}")

        print(f"[3] Nucleotide Frequency: {self.count_nuc()}")

        print(f"[4] DNA -> RNA Transcription: {coloured(self.transcript())}")

        # [5] was pretty much copied from this commit as it was awesome
        # https://gitlab.com/RebelCoder/dna-toolset/-/commit/8a4be0e3a70733be9bebdf0d9eed987c0fb44429
        print("[5] Reverse Complement:\n")
        print(f"5' {coloured(self.seq)} 3'")
        print(f"   {''.join(['|' for c in range(len(self.seq))])}")
        print(f"3' {coloured(self.complement())} 5' [Complement]")
        print(f"5' {coloured(self.reverse_complement())} 3' [Reverse Complement]\n")
        
        print(f"[6] GC Content: {self.gc_content()}%")

    # Function should return the frequency of each nucleotide
    def count_nuc(self):
        """Counts the nucleotide frequency within an imported DNA sequence"""
        freq_dict = {"A" : 0, "G" : 0, "T" : 0, "C" : 0}
        # Ensures dna_seq that is checked is in uppercase form
        # For each nucleotide, add to dict where key = nuc
        for nuc in self.seq:
            freq_dict[nuc] += 1
        return freq_dict
    
    # Simple function to transcript a DNA sequence into its RNA counterpart
    # TLDR: Replaces Thyamine with Uracil
    def transcript(self):
        """Transcripts an imported DNA sequence into its RNA counterpart"""
        return self.seq.replace("T", "U")
    
    # Complement finder - Find complement string via nuc_complements
    def complement(self):
        """Finds the reverse complement of an imported DNA sequence"""
        complement = ''
        for nuc in self.seq:
            # Find the complement for the nucleotide, add it to the string
            # Ensures uppercase lettering
            complement += nuc_complements[nuc.upper()]
        return complement
    
    # Reverse complement - calls complement, reverses + returns output
    def reverse_complement(self):
        """Returns the reverse of the complement function output"""
        return self.complement()[::-1]

    # Simple function to return GC content of an DNA sequence
    def gc_content(self):
        """Function to return GC content of an imported DNA sequence"""
        return round(((self.seq.count("G") + self.seq.count("C")) / len(self.seq)) * 100)
