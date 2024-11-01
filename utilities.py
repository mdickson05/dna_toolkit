# Copied directly from https://gitlab.com/RebelCoder/dna-toolset/
# Colourises nucleotides within DNA sequence
def coloured(seq):
    """Colourises nucleotides within DNA sequence"""
    # Dictionary of colour codes for each letter
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    # No need to validate string for colouring - just won't colour invalid strings
    for nuc in seq:
        if nuc in bcolors:
            # If in dictionary, nuc with colour code added
            tmpStr += bcolors[nuc] + nuc
        else:
            # If not in dictionary, reset to default colour
            tmpStr += bcolors['reset'] + nuc
    # Return tmpStr with reset char at end to signify EOF
    return tmpStr + '\033[0;0m'

# Read/write text files
def readTextFile(path):
    """Read text file from specified path"""
    with open(path, 'r') as f:
        return "".join([l.strip() for l in f.readlines()])
    
def writeTextFile(path, seq, mode="w"):
    """Write/append imported sequence to specified file path"""
    with open(path, mode) as f:
        f.write(seq + "\n")

# read FASTA files
def read_FASTA(path):
    with open(path, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line

    return FASTADict
