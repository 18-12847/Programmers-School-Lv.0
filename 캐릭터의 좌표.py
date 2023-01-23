def solution(keyinput, board):
    ans =[0, 0]
    for i in keyinput:
        if i == "left" and -int(board[0]/2) < ans[0] <= int(board[0]/2):
            ans[0] -= 1
        elif i == "right" and -int(board[0]/2) <= ans[0] < int(board[0]/2):
            ans[0] += 1
        elif i == "up" and -int(board[1]/2) <= ans[1] < int(board[1]/2):
            ans[1] += 1
        elif i == "down" and -int(board[1]/2) < ans[1] <= int(board[1]/2):
            ans[1] -= 1
    return ans