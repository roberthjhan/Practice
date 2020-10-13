"""
Problem
A permutation of length n is an ordering of the positive integers
{1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a
list of all such permutations (in any order).
"""
import itertools

def enumerate(n):
    l = []
    while n > 0:
        l.append(n)
        n -= 1
    return l

def pretty_return(lst):
    ret = ""
    for tup in lst:
        for n in tup:
            ret += str(n) + " "
        ret += "\n"
    return ret

def main():
    filename = "rosalind_perm.txt"
    n = open(filename, "r").read()

    l = list(itertools.permutations(enumerate(n)))

    print(len(l))
    print(pretty_return(l))

main()