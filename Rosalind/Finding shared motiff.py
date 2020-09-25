"""
Problem
A common substring of a collection of strings is a substring of
every member of the collection. We say that a common substring
is a longest common substring if there does not exist a longer
common substring. For example, "CG" is a common substring of
"ACGTACGT" and "AACCGTATA", but it is not as long as possible;
in this case, "CGTA" is a longest common substring of "ACGTACGT"
and "AACCGTATA".

Note that the longest common substring is not necessarily unique;
for a simple example, "AA" and "CC" are both longest common
substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1
kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple
solutions exist, you may return any single solution.)

Comments:

This solution iterates through every possible substring in each sequence.
A better solution might only check the substrings in the first sequence
then check the other sequences to see if it is common to all.

This solution also starts with the smallest substrings. A better solution
implementing the better algorithm would start with the largest substrings
then return the first one found.
"""

def organizeData(data):
    """
    Organize data into a list of lists. Sublists are sequences of
    the file's FASTA sequences. Do not store/return FASTA IDs.
    """
    ret = []
    for line in data:
        if line[0] != ">":
            ret[-1] += line.rstrip("\n")
        else: ret.append("") # New FASTA ID add new sequence
    return ret

def countMotiff(data):
    """
    Count motiffs. For each sequence make a sliding window and increment count.
    If the substring in that sliding window exists in common update value to count.
    After each sequence is checked remove any substrings with values less than
    current count (substrings not common to all sequences checked so far).
    """
    common = {}
    count = 0
    for seq in data:
        count += 1
        for n in range(len(seq)):
            for m in range(len(seq)):
                substring = seq[n:m]
                if substring in common: # and common[substring] >= count - 1: I think second part not needed.
                    # > count-1 dup found in current sequence
                    # = count -1 new common found
                    common[substring] = count
                else:
                    if count == 1 and substring!= "": # Add all substrings from first sequence to common
                        common[substring] = count
        print(f"Seq {count}/{len(data)}") # Show progress
        # After each sequence is checked remove substrings not common to all sequences checked so far
        common = {k: v for k, v in common.items() if v == count}
    return common

def longestMotiff(common):
    """
    Find longest common motiff by checking the length of keys in common.
    """
    longest = ""
    for key in common.keys():
        if len(key) > len(longest):
            longest = key
    return longest

filename = "rosalind_lcsm.txt"
data = open(filename, "r")
data = organizeData(data)
commonSeqs = countMotiff(data)
print(longestMotiff(commonSeqs))