"""
https://leetcode.com/problems/unique-paths-ii/

My code works but I keep failing a testcase where one subarray of the array is smaller
than the rest. Not sure how to proceed at this point so I'm saving and coming back to it.
"""
def uniquePath(obstacleGrid):
    if obstacleGrid[0][0] == 1: # start position is blocked, len(arr) = 1, len(arr[0]) = 1
        return 0

    def move(obstacleGrid, cur, dest):
        if cur == dest:
            return 1
        if obstacleGrid[cur[0]][cur[1]] == 1:
            return 0

        count = 0
        down = (cur[0] + 1, cur[1])
        right = (cur[0], cur[1] + 1)

        if down[0] <= dest[0] and obstacleGrid[down[0]][down[1]] == 0:
            count += move(obstacleGrid, down, dest)
        if right[1] <= dest[1] and obstacleGrid[right[0]][right[1]] == 0:
            count += move(obstacleGrid, right, dest)
        return count

    cur = (0, 0)  # y,x
    dest = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)

    return move(obstacleGrid, cur, dest)


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePath(obstacleGrid))