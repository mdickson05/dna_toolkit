from constants import * 
from utilities import coloured
from collections import Counter
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
    def generate(self, length=20, type="DNA"):
        """Generate random valid sequence"""
        seq = ''.join([random.choice(nucleotide_base[type]) for nuc in range(length)])
        self.__init__(seq, type, "Randomly Generated Sequence")


    # Simple check whether sequence is valid DNA string
    def __validate(self, seq):
        """Simple check to see whether the imported DNA string is valid"""
        # Ensure imported sequence is uppercase
        to_check = seq.upper()
        for nuc in to_check:
            if nuc not in nucleotide_base[self.type]:
                return False
        return True

    # Simple "to string" method for the sequence itself
    def __describe(self):
        """Returns basic sequence info"""
        return f"\n[Label] {self.label}\n[Sequence] {coloured(self.seq)}\n[Type] {self.type}\n[Is valid?] {self.is_valid}\n"


    def print_info(self):
        """Prints all available information for sequence"""
        
        print("[1] Sequence Information")
        print(self.__describe())

        print(f"[2] Length: {len(self.seq)}")

        print(f"[3] Nucleotide Frequency: {self.count_nuc()}")

        if self.type == "DNA":
            print(f"[4] DNA -> RNA Transcription: {coloured(self.transcript())}")
        else:
            print("[4] DNA -> RNA Transcription: Not a DNA sequence")

        # [5] was pretty much copied from this commit as it was awesome
        # https://gitlab.com/RebelCoder/dna-toolset/-/commit/8a4be0e3a70733be9bebdf0d9eed987c0fb44429
        print("[5] Reverse Complement:\n")
        print(f"5' {coloured(self.seq)} 3'")
        print(f"   {''.join(['|' for c in range(len(self.seq))])}")
        print(f"3' {coloured(self.complement(self.seq))} 5' [Complement]")
        print(f"5' {coloured(self.reverse_complement(self.seq))} 3' [Reverse Complement]\n")
        
        print(f"[6] GC Content: {self.gc_content(self.seq)}%")

        print(f"[7] GC Content of subsequences (window size = 5): {self.gc_content_subseq(5)}")
        
        print(f"[8] Amino Acids Sequence from DNA sequence: {self.translate(self.seq, 0)}")

        print(f"[9] Codon frequency (L): {self.codon_frequency("L")}")

        print("[10] Reading frames:")
        rfs = self.generate_reading_frames(self.seq)
        for frame in rfs:
            print(frame)

        print("[11] Available proteins:")
        all_prots = self.all_proteins(0, 0, True)
        if all_prots != []:
            for prot in all_prots:
                print(f"{prot}")
        else:
            print("No proteins found")

        

    # Function should return the frequency of each nucleotide
    def count_nuc(self):
        """Counts the nucleotide frequency within an imported DNA sequence"""
        if self.type == "DNA":
            freq_dict = {"A" : 0, "G" : 0, "T" : 0, "C" : 0}
        elif self.type == "RNA":
            freq_dict = {"A" : 0, "G" : 0, "U" : 0, "C" : 0}
        # Ensures dna_seq that is checked is in uppercase form
        # For each nucleotide, add to dict where key = nuc
        for nuc in self.seq:
            freq_dict[nuc] += 1
        return freq_dict
    
    # Simple function to transcript a DNA sequence into its RNA counterpart
    # TLDR: Replaces Thyamine with Uracil
    def transcript(self):
        """Transcripts an imported DNA sequence into its RNA counterpart"""
        if self.type == "DNA":
            return self.seq.replace("T", "U")
        else:
            return "Not a valid DNA sequence - cannot transcript"
    
    # Complement finder - Find complement string via nuc_complements
    def complement(self, seq):
        """Finds the reverse complement of an imported DNA sequence"""
        complement = ''
        for nuc in seq:
            # Find the complement for the nucleotide, add it to the string
            # Ensures uppercase lettering
            complement += nuc_complements[self.type][nuc.upper()]
        return complement
    
    # Reverse complement - calls complement, reverses + returns output
    def reverse_complement(self, seq):
        """Returns the reverse of the complement function output"""
        return self.complement(seq)[::-1]

    # Simple function to return GC content of an DNA sequence
    def gc_content(self, seq):
        """Function to return GC content of an imported DNA sequence"""
        return round(((seq.count("G") + seq.count("C")) / len(seq)) * 100)
    
    # Function that calculates the GC content for a specific window of nucleotides
    # i.e. if len(seq) = 20, and k = 5, will find GC content for 1-5, 6-10, etc.
    def gc_content_subseq(self, window_size):
        """Given imported window size, find the GC content of each subsequence within 
        each window for an imported DNA sequence"""
        res = []
        # for i in range 0 to len(seq) - window_size + 1
        # Each iteration, i increases by window_size
        for i in range(0, len(self.seq) - window_size + 1, window_size):
            # subseq is between current i value and i + window_size
            subseq = self.seq[i : i + window_size]
            res.append(self.gc_content(subseq))
        return res
    
    # Function that translates imported DNA sequence to amino acid codons
    def translate(self, seq, init_pos):
        """Imports a DNA sequence and a starting position to translate a DNA string 
        into amino acid codons"""
        codons = []
        # Starts at init_pos, finishes at len(seq) - 2 (to avoid reading 
        # past the last triplet), increments by 3.
        for pos in range(init_pos, len(seq) - 2, 3):
            if self.type == "DNA":
                codons.append(dna_codons[seq[pos:pos+3]])
            elif self.type == "RNA":
                codons.append(rna_codons[seq[pos:pos+3]])
        return codons
    
    # Function that returns a frequency map of an imported amino acid within a DNA sequence
    def codon_frequency(self, amino_acid):
        """Returns a frequency map of an imported amino acid within an imported DNA sequence"""
        temp_list = []
    # Starts at init_pos, finishes at len(seq) - 2 (to avoid reading past the last triplet), increments by 3.
        for i in range(0, len(self.seq) - 2, 3):
            # Sequence to check is between i and i + 3
            to_check = self.seq[i:i+3]
            # If the codon value of to_check chars matches the imported amino_acid
            if self.type == "DNA":
                if dna_codons[to_check] is amino_acid:
                    # add to temporary list
                    temp_list.append(to_check)
            elif self.type == "RNA":
                if rna_codons[to_check] is amino_acid:
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

    def generate_reading_frames(self, seq):
        """Generates reading frames for imported sequence"""
        frames = []
        # Frames starting from each possible init_pos (without excluding data)
        frames.append(self.translate(seq, 0))
        frames.append(self.translate(seq, 1))
        frames.append(self.translate(seq, 2))
        # Reverse complement frames
        frames.append(self.translate(self.reverse_complement(seq), 0))
        frames.append(self.translate(self.reverse_complement(seq), 1))
        frames.append(self.translate(self.reverse_complement(seq), 2))

        return frames
    
    # Function that finds the list of proteins within an amino acid sequence
    def find_rf_proteins(self, aa_seq):
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
    
    # Function to find all proteins within a given range
    def all_proteins(self, startPos, endPos, ordered):
        """Given a start and end position, finds all proteins within a sequence"""
        # If there IS an start and end
        if endPos > startPos:
            rfs = self.generate_reading_frames(self.seq[startPos : endPos])
        # If endPos and startPos are both == 0
        elif endPos == startPos == 0:
            rfs = self.generate_reading_frames(self.seq)
        # If endPos < startPos == invalid
        else:
            print("Error: invalid startPos/endPos - cannot generate frames!")
            return

        res = []
        for rf in rfs:
            prots = self.find_rf_proteins(rf)
            for p in prots:
                res.append(p)

        if ordered:
            # Sort list by results, where key is the item's length 
            # and the list is descending
            return sorted(res, key=len, reverse=True)
        return res
