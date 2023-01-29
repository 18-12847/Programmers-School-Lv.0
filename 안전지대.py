def solution(board):
    if  board[0][0] == 1 and len(board) * len(board) == 1:
        return 0
    if  board[0][0] == 0 and len(board) * len(board) == 1:
        return 1
    tmp = [[0 for j in range(len(board))] for i in range(len(board))]
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 and i == 0 and j == 0:
                tmp[i][j+1] = 1
                tmp[i+1][j] = 1
                tmp[i+1][j+1] = 1
            elif board[i][j] == 1 and i == 0 and j == len(board)-1:
                tmp[i][j-1] = 1
                tmp[i+1][j] = 1
                tmp[i+1][j-1] = 1
                break
            elif board[i][j] == 1 and i == len(board)-1 and j == 0:
                tmp[i-1][j] = 1
                tmp[i][j+1] = 1
                tmp[i-1][j+1] = 1
                break
            elif board[i][j] == 1 and i == len(board)-1 and j == len(board)-1:
                tmp[i-1][j] = 1
                tmp[i][j-1] = 1
                tmp[i-1][j-1] = 1
                break
            elif board[i][j] == 1 and i == 0:
                tmp[i][j-1] = 1
                tmp[i][j+1] = 1
                tmp[i+1][j-1] = 1
                tmp[i+1][j] = 1
                tmp[i+1][j+1] = 1
            elif board[i][j] == 1 and j == 0:
                tmp[i-1][j] = 1
                tmp[i-1][j+1] = 1
                tmp[i][j+1] = 1
                tmp[i+1][j] = 1
                tmp[i+1][j+1] = 1
            elif board[i][j] == 1 and i == len(board)-1:
                tmp[i][j-1] = 1
                tmp[i-1][j-1] = 1
                tmp[i-1][j] = 1
                tmp[i-1][j+1] = 1
                tmp[i][j+1] = 1
            elif board[i][j] == 1 and j == len(board)-1:
                tmp[i-1][j-1] = 1
                tmp[i-1][j] = 1
                tmp[i][j-1] = 1
                tmp[i+1][j-1] = 1
                tmp[i+1][j] = 1
            elif board[i][j] == 1:
                tmp[i][j+1] = 1
                tmp[i][j-1] = 1
                tmp[i+1][j] = 1
                tmp[i-1][j] = 1
                tmp[i+1][j+1] = 1
                tmp[i-1][j-1] = 1
                tmp[i-1][j+1] = 1
                tmp[i+1][j-1] = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                cnt += 1
            elif tmp[i][j] == 1:
                cnt += 1
    return len(board) * len(board) - cnt