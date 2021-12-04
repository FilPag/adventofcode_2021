import re

def append_board(line, board):
  line = re.sub(" +", " ", line)
  line = line.strip()
  row = line.split(" ")

  for i in range(len(row)):
    row[i] = (row[i], False)

  board.append(row)
  return board

def checkWins(board):
  col_wins = [True for _ in range(len(board[0]))]
  
  for r in board:
    row_win = True
    for i, c in enumerate(r):
      col_wins[i] = col_wins[i] and c[1]
      row_win = row_win and c[1]
    if row_win:
      return True

  for i in col_wins:
    if i:
      return True

  return False

def check_number(board, number):
  for i in range(len(board)):
    for j in range(len(board[i])):
      pos = board[i][j][0]
      if pos == number:
        board[i][j] = (pos, True)

def process_input(boards, input):
  winners = []
  for board in boards:
    check_number(board, input)
    win = checkWins(board)  
    if win:
      winners.append(board)
  return winners 

def find_sum(board):
  s = 0
  for r in board:
    for c in r:
      if not c[1]:
        s += int(c[0])
  return s 

file = open('input.txt', "r")
inputs = file.readline().rstrip()
inputs = inputs.split(",")
boards = []
for line in file:
  line = line.rstrip()
  if line == "":
    boards.append([])
  else:
    board = append_board(line, boards[-1]) 

for i in inputs:
  winners = process_input(boards, i)

  if winners == boards:
    s = find_sum(boards[-1])
    print(f"Score of last winner: {s * int(i)}")
    break

  if len(winners) > 0:
    for w in winners:
      boards.remove(w)
