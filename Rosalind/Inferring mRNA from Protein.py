'''
For positive integers a and n, a modulo n (written amodn in shorthand) is the
remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and
division with respect to the modulo operation. We say that a and b are congruent
modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn,
then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules,
you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large)
integer solution modulo a smaller number to avoid the computational pitfalls that arise
with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have
been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in
protein translation.)
'''

freq = {'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 'S': 6, 'P': 4,
        'T': 4, 'A': 4, 'Y': 2, 'H': 2, 'N': 2, 'D': 2, 'Stop': 3,
        'Q': 2, 'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1}

def numRNA(protein):
    ct = 3 # Initialize with 3 bc 3 stop codons
    for aa in protein:
        if aa in freq:
            ct *= freq[aa]
    return ct % 1000000

filename = "rosalind_mrna.txt"
protein = open(filename, "r").read()
print(numRNA(protein))