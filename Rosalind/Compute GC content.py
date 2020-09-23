"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in
the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG"
is 37.5%. Note that the reverse complement of any DNA string has the same
GC-content.

DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format. In this
format, the string is introduced by a line that begins with '>', followed
by some labeling information. Subsequent lines contain the string itself;
the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by
the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000
and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in
all decimal answers unless otherwise stated; please see the note on absolute
error below.
"""


def calcGC(dna):
    """ Calculate gc content"""
    return ((dna.count("G") + dna.count("C"))/len(dna)) * 100

def method1():
    filename = "rosalind_gc.txt"
    genes = {} # ID: GC Content
    data = open(filename, "r").read()
    data = data.replace("\n", "") # Remove newline characters
    data = data.split(">") # Split strings by ID

    for dna in data:
        if "Rosalind" in dna:
            genes[dna[:13]] = calcGC(dna[13:])

    id = None
    gc = 0
    
    for key in genes.keys():
        if genes[key] > gc:
            id = key
            gc = genes[key]
    # Need to return a percent
    return f"{id}\n{gc}"

def method2():
    filename = "rosalind_gc.txt"
    genes = {}  # ID: GC Content
    data = open(filename, "r")

    id = None
    gc = 0

    for line in data:
        line = line.replace("\n", "")
        if line[0] == ">":
            id = line[1:]
            genes[id] = ""
        else:
            genes[id] += line

    for key in genes.keys():
        genes[key] = calcGC(genes[key])
        if genes[key] > gc:
            id = key
            gc = genes[key]

    # Need to return a percent
    return f"{id}\n{gc}"

print(method1())
print(method2())