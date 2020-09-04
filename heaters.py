"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all
the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all
houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum
radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

https://leetcode.com/problems/heaters/


Two solutions are listed because one is mine and the other is a published answer I don't think I would've been able to
come up with myself.
"""


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        I recently learned about sets so I wanted to write a solution using sets.
        The algorithm is generating a set of points the heaters reach and then checking whether the list of
        houses is a subset of the heaters. When it's not the heater's range is incremented by 1 and a new set is generated.

        Admittedly spacewise and timewise it's not ideal especially when the distance between houses gets bigger but I
        wanted to practice with sets and I suppose I achieved that goal.
        """
        houses = set(houses)
        # If a all houses share a location with a heater
        if houses.issubset(set(heaters)):
            return 0

        n = 1
        heat_range = heaters + [x + 1 for x in heaters] + [x - 1 for x in heaters if x - 1 > 0]
        # While there are houses outside of the heater range, increment range and update the list
        while not houses.issubset(set(heat_range)):
            n += 1
            heat_range = heat_range + [x + n for x in heaters] + [x - n for x in heaters if x - n > 0]

        return n

def findRadius(houses, heaters):
        """
        Published solution with my own annotations explaining steps.
        credit: axelramar9
        """
        houses.sort() # At least one test case has an unsorted list
        heaters.sort()
        N, i, maxRadius = len(heaters), 0, 0
        # Find the closest left and right heater for each house i = left, i+1 = right
        for house in houses:
            while i+1 < N and heaters[i+1] < house:
                i += 1
            # With the heaters found update value of maxRadius
            maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))
            # maxRadius = the greater of the last maxRadius found and closest heater
            # Remember in list splicing stop is not inclusive
        return maxRadius