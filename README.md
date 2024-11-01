# Bioinformatics Projects
A list of projects I created to understand basics of bioinformatics.

Followed the "Bioinformatics in Python" Youtube series from rebelScience:
https://www.youtube.com/@rebelScience

## Features
### sequences.py
*  Sequence Information: Includes a description of a given sequence, including the specific DNA/RNA string, its label and its type (DNA or RNA).
*  Transcription: Convert DNA -> RNA
*  Complements and Reverse Complements
*  GC content for full sequence and
*  GC content for subsequences of the main sequence given a window size
*  Translation: Convert DNA/RNA nucleotides triplets to codons.
*  Codon frequency: Find the frequency of a given codon in a sequence
*  Generate reading frames
*  Find all available proteins (can import startPos and endPos for flexibility)
*  Print sequence info: prints all of the above in a nice, readable format
### utilities.py
*  Coloured terminal output: each nucleotide is coloured when displayed to the user
*  Read/write support from text files
*  Read support for FASTA-formatted text files
