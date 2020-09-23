"""
Problem

Given two strings s and t of equal length, the Hamming distance
between s and t, denoted dH(s,t), is the number of corresponding
symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

def dH(s, t):
    distance = 0
    for n in range(len(s)):
        if s[n] != t[n]:
            distance += 1
    return distance

filename = "rosalind_hamm.txt"
data = open(filename, "r")
s = data.readline().replace("\n", "")
t = data.readline()

print(dH(s, t))
