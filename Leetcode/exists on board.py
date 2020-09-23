"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Mark visited coordinates during each run, if a solution isn't found unmark them.
https://leetcode.com/problems/word-search/
"""
def exist(board, word):
    '''dfs problem'''
    max_y = len(board) -1
    max_x = len(board[0])-1

    def dfs(index, s, board):
        # Basecase
        if s == "":
            return True
        # Mark visited
        temp = str(board[index[0]][index[1]])
        board[index[0]][index[1]] = "#"
        # Check up/down/left/right for valid moves
        for y, x in (index[0] - 1, index[1]), (index[0] + 1, index[1]), (index[0], index[1] - 1), (index[0], index[1] + 1):
            if 0 <= y <= max_y and 0 <= x <= max_x and s[0] == board[y][x]:
                if dfs((y,x), s[1:], board):
                    return True
        # Unmark visited
        board[index[0]][index[1]] = temp
        return False

    # Iterate looking for starting points (word[0])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if board[y][x] == word[0]:
                s = word[1:]
                if dfs((y,x), s, board):
                    return True
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
board2 = [["a", "a"]]
board3 = [["C","A","A"],
          ["A","A","A"],
          ["B","C","D"]]


print(exist(board, "SEED"))
print(exist(board2, "aaa"))
print(exist(board3, "AAB"))
