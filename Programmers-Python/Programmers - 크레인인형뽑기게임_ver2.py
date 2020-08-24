def solution(board, moves):
    answer = 0
    crane = []

    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move]:
                if not crane :
                    crane.append(board[i][move])
                else:
                    craneData = crane.pop()
                    if craneData == board[i][move]:
                        answer += 2
                    else:
                        crane.append(craneData)
                        crane.append(board[i][move])
                board[i][move] = 0
                break
    return answer


if __name__ == "__main__":
  board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
  moves = [1,5,3,5,1,2,1,4]
  print( solution(board, moves))