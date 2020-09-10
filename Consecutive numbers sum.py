"""
Given a positive integer N, how many ways can we write it as a sum of
consecutive positive integers?

I solved it with a brute force method and got stuck with optimizing the
algorithm for larger Ns.

I guess this question was pretty hard not many answers in python.
One solution used bitwise operators which I'm not terribly familiar with,
the other wasn't well documented so I'll have to go through the logic on
that one later.

My solution:
Main logic is that we'll never use a number greater than N//2 + 1 so create
list: l based on that. Iterate through l and create a sliding window keeping
track of the sum of that window. When sum >= N break the while loop and increment the window.

"""
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 0:
            return 0
        l = [n for n in range(N // 2 + 2)]
        count = 1 # Start at 1 because N by itself counts as a consecutive
                    # number sum according to the problem.

        for i in l:
            n = 0
            sum = 0
            while sum < N and i < max(l):
                cur = l[i + n]
                sum += cur
                n += 1
                if sum == N:
                    count += 1

        return count

def good_sol(N):
    import math
    uplimt = int(math.sqrt(2*N))
    rlt = 0
    for n in range(uplimt):
        if 2*N % (n+1) == 0 and (2*N/(n+1)-n) % 2 == 0:
            rlt += 1
    return rlt