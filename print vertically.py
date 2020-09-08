"""
Another ugly one but pretty close to what others had.
Goal for this was strange... Take a sentence and return it
vertically so 'The fat cat eats' is like:
T H E
F A T
C A T
E A T S
But it needs to be returned as
['Tfce', 'haaa', 'ettt', '   s']
"""

def printVertically(s: str) :
    s = s.split(" ")
    # Length of return list = longest word in string
    longest = max([len(i) for i in s])
    ret = [""] * longest # Create spaces for our words
    cur = 0
    while cur < len(s): # Actually, bad use of while loop. Should be for since len(s) is known
        s[cur] += " " * (longest - len(s[cur])) # Add missing spaces
        for i in range(len(s[cur])): # Add letters
            ret[i] += s[cur][i]
        cur += 1
    # Remove trailing spaces
    for n in range(len(ret)):
        while ret[n][-1] == " ":
            ret[n] = ret[n][:-1]
    # Return solution
    return ret
