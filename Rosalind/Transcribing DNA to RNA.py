"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u
is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

t = open("rosalind_rna.txt").read()
for n in range(len(t)):
    if t[n] == "T":
        # Strings are immutable, to change the Ts to Us we can construct a "new" string
        # by splicing the old one.
        t = t[:n] + "U" + t[n+1:]
print(t)