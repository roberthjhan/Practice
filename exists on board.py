"""
Problem:
Temp board isn't being treated as a unique instance and changes to it
are being reflected to board.
Have tried board.copy() and board[:] to no avail

Will come back later


"""


def exist(board, word):
    '''dfs problem'''
    max_y = len(board) -1
    max_x = len(board[0])-1

    def dfs(index, s, temp_board):
        if s == "":
            return True

        for y, x in (index[0] - 1, index[1]), (index[0] + 1, index[1]), (index[0], index[1] - 1), (index[0], index[1] + 1):
            if 0 <= y <= max_y and 0 <= x <= max_x and s[0] == temp_board[y][x]:
                temp_board[y][x] = "#" # Mark visited indices for this run
                if dfs((y,x), s[1:], temp_board):
                    return True
        return False

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(board)
            if board[y][x] == word[0]:
                temp_board = board[:]

                temp_board[y][x] = "#"
                s = word[1:]
                if dfs((y,x), s, temp_board):

                    for i in board:
                        print(i)
                    return True
    for i in board:
        print(i)
    return False




board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
board2 = [["a", "a"]]
board3 = [["C","A","A"],
          ["A","A","A"],
          ["B","C","D"]]


# print(exist(board, "SEED"))
# print(exist(board2, "aaa"))
print(exist(board3, "AAB"))
