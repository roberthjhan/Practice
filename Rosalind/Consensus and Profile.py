"""

Problem
A matrix is a rectangular table of values divided into rows and columns.
An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j
to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number
of times that 'A' occurs in the jth position of one of the strings, P2,j
represents the number of times that C occurs in the jth position, and so on
(see below).

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""

def getConsensus(data):
    """
    Using the organized data generate profile matrix as a dictionary, and
    consensus string.
    """
    profile_matrix = {
        "A": [0] * len(data[0]),
        "C": [0] * len(data[0]),
        "G": [0] * len(data[0]),
        "T": [0] * len(data[0])}
    consensus = ""

    # Iterate through the nth element of each sequence.
    for n in range(len(data[0])):
        for line in data:
            profile_matrix[line[n]][n] += 1
        # Find consensus nucleotide for the nth element.
        consensus += mostCommon([[key for key in profile_matrix.keys()],
                           [profile_matrix[key][n] for key in profile_matrix.keys()]])

    return profile_matrix, consensus

def mostCommon(counts):
    """
    Return first nucleotide at max count (str).
    counts[0] = ["A", "C", "G", "T"]
    counts[1] = [count for each nucleotide in order of counts[0]]
    """
    m = max(counts[1])
    for i, j in enumerate(counts[1]): # i = index, j = count
        if j == m:
            return counts[0][i]

def printReslt(profile):
    """
    Print results so it can be nicely copy pasted to Rosalind.
    """
    ret = ""
    for key in profile.keys():
        temp = f"{str(key)}: "
        for n in profile[key]:
            temp += f"{str(n)} "
        ret += f"{temp}\n"
    return(ret)

def organizeData(data):
    """
    Organize data into a list of lists. Sublists are sequences of
    the file's FASTA sequences. Do not store/return FASTA IDs.
    """
    ret = []
    for line in data:
        if line[0] != ">":
            ret[-1] += line.rstrip("\n")
        else: ret.append([]) # New FASTA ID add new sequence
    return ret

filename = "rosalind_cons.txt"
data = open(filename, "r")
data = (organizeData(data))
profile, consensus = getConsensus(data)

print(consensus)
print(printReslt(profile))