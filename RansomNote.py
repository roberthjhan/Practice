"""
Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Solution: using a dictionary create a count of all available letters in magazine.
Iterating through the ransomNote, if the letter is in stock decrement the count
for that letter. If the count becomes < 0 return False. If the letter isn't in
the dictionary return False.

Looking at the solutions, I have yet again forgotten we can import modules.
Another solution would be to import the Counter module from collections which
returns a dictionary very similar to what was set up with have. Logic is approximately
the same though.

"""
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == "": # No letters needed
            return True
        elif magazine == "": # Letters needed none available
            return False

        have = {}
        # Take stock of what letters can be used and how many times
        for char in magazine:
            if char in have.keys():
                have[char] += 1
            else:
                have[char] = 1
        # Check if note can be written
        for char in ransomNote:
            if char in have.keys():
                have[char] -= 1
                if have[char] < 0: # Letter not available
                    return False
            else: # Letter not available
                return False
        return True