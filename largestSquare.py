"""
This is actually a really cool problem. I first saw it on Leetcode a couple days
ago and was really lost with how to proceed. Then just out of the blue I stumbled
upon a really good video of someone working through the problem using dynamic
programming. After watching him explain the algorithm it clicked for me and I was
able to write it out. This question in particular has really furthered my
understanding of dynamic programming and how to approach problems.

Dynamic programming is a technique by which recomputation is minimized by storing the
results of subproblems. This is a tradeoff of time for space.

In this question we iterate through the array with the assumption that each itterant is
the bottom right corner of a square. We then calculate the value of that square by checking
the other corners. In doing so we go from:

[1, 1, 0, 1, 0]
[0, 1, 1, 1, 0]
[1, 1, 1, 1, 0]
[0, 1, 1, 1, 1]
--------------------
[1, 1, 0, 1, 0]
[0, 1, 1, 1, 0]
[1, 1, 2, 2, 0]
[0, 1, 2, 3, 1]

The solution is the max of the max of each row.

https://www.geeksforgeeks.org/dynamic-programming/
https://www.youtube.com/watch?v=FO7VXDfS8Gk
"""
def largestSquare(arr):
    """Solve each square and save it"""
    c = arr # Cache for storing computations
    for i in c:
        print(i)
    # Won't touch arr[0] or arr[n][0] because they can't be bottom right corners
    for row in range(1, len(arr)):
        for col in range(1, len(arr[0])):
            if arr[row][col] > 0: # 0s can't make squares
                c[row][col] = min(c[row-1][col-1], c[row][col-1], c[row-1][col]) + arr[row][col]
                # Minimum of surrounding squares + current square = maximum size square
    print("-" *20)
    for i in c:
        print(i)
    return max([max(i) for i in c])

arr = [[1,1,0,1,0],
       [0,1,1,1,0],
       [1,1,1,1,0],
       [0,1,1,1,1]]
print(largestSquare(arr))