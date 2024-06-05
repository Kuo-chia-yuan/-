import random

def create():
  list1 = [['.' for i in range(10)] for j in range(10)]
  return list1

def see(board):
  print('  0 1 2 3 4 5 6 7 8 9')
  for i in range(10):
    print(i, end = ' ')
    for j in range(10):
      print(board[i][j], end = ' ')
    print()
  print('---------------------')

def computer(board):
  # 防邊緣四
  for i in range(0, 10):
    if board[i][0]==board[i][1]==board[i][2]==board[i][3]=='O':
      if board[i][4]=='.':
        board[i][4] = 'X'
        return 0
    if board[i][6]==board[i][7]==board[i][8]==board[i][9]=='O':
      if board[i][5]=='.':
        board[i][5] = 'X'
        return 0

  for i in range(0, 10):
    if board[0][i]==board[1][i]==board[2][i]==board[3][i]=='O':
      if board[4][i]=='.':
        board[4][i] = 'X'
        return 0
    if board[6][i]==board[7][i]==board[8][i]==board[9][i]=='O':
      if board[5][i]=='.':
        board[5][i] = 'X'
        return 0

  for i in range(0, 6):
    if board[0][i]==board[1][i+1]==board[2][i+2]==board[3][i+3]=='O':
      if board[4][i+4]=='.':
        board[4][i+4] = 'X'
        return 0
    if board[6][i+1]==board[7][i+2]==board[8][i+3]==board[9][i+4]=='O':
      if board[5][i]=='.':
        board[5][i] = 'X'
        return 0

  for i in range(0, 6):
    if board[3][i+1]==board[2][i+2]==board[1][i+3]==board[0][i+4]=='O':
      if board[4][i]=='.':
        board[4][i] = 'X'
        return 0
    if board[9][i]==board[8][i+1]==board[7][i+2]==board[6][i+3]=='O':
      if board[5][i+4]=='.':
        board[5][i+4] = 'X'
        return 0
  
  # 防死四
  for i in range(1, 9):
    for j in range(1, 6):
      if board[i][j]==board[i][j+1]==board[i][j+2]==board[i][j+3]=='O':
        if board[i][j-1]=='.':
          board[i][j-1] = 'X'
          return 0
        if board[i][j+4]=='.':
          board[i][j+4] = 'X'
          return 0

  for i in range(1, 6):
    for j in range(1, 9):
      if board[i][j]==board[i+1][j]==board[i+2][j]==board[i+3][j]=='O':
        if board[i-1][j]=='.':
          board[i-1][j] = 'X'
          return 0
        if board[i+4][j]=='.':
          board[i+4][j] = 'X'
          return 0
  
  for i in range(1, 6):
    for j in range(1, 6):
      if board[i][j]==board[i+1][j+1]==board[i+2][j+2]==board[i+3][j+3]=='O':
        if board[i-1][j-1]=='.':
          board[i-1][j-1] = 'X'
          return 0
        if board[i+4][j+4]=='.':
          board[i+4][j+4] = 'X'
          return 0

  for i in range(1, 6):
    for j in range(4, 9):
      if board[i][j]==board[i+1][j-1]==board[i+2][j-2]==board[i+3][j-3]=='O':
        if board[i-1][j+1]=='.':
          board[i-1][j+1] = 'X'
          return 0
        if board[i+4][j-4]=='.':
          board[i+4][j-4] = 'X'
          return 0

  # 防活三
  for i in range(1, 9):
    for j in range(1, 7):
      if board[i][j]==board[i][j+1]==board[i][j+2]=='O' and board[i][j-1]==board[i][j+3]=='.':
        board[i][j-1] = 'X'
        return 0
  
  for i in range(1, 7):
    for j in range(1, 9):
      if board[i][j]==board[i+1][j]==board[i+2][j]=='O' and board[i-1][j]==board[i+3][j]=='.':
        board[i-1][j] = 'X'
        return 0

  for i in range(1, 7):
    for j in range(1, 7):
      if board[i][j]==board[i+1][j+1]==board[i+2][j+2]=='O' and board[i-1][j-1]==board[i+3][j+3]=='.':
        board[i-1][j-1] = 'X'
        return 0

  for i in range(1, 7):
    for j in range(3, 9):
      if board[i][j]==board[i+1][j-1]==board[i+2][j-2]=='O' and board[i-1][j+1]==board[i+3][j-3]=='.':
        board[i-1][j+1] = 'X'
        return 0

  empty = [[i, j] for i in range(10) for j in range(10) if board[i][j] == '.']
  row, col = random.choice(empty)
  board[row][col] = 'X'

def user(board):
  row = int(input('行：'))
  col = int(input('列：'))
  board[row][col] = 'O'

def win_loss(board):
  for i in range(10):
    for j in range(6):
      if board[i][j]==board[i][j+1]==board[i][j+2]==board[i][j+3]==board[i][j+4]=='O':
        print('you win')
        return True
      if board[j][i]==board[j+1][i]==board[j+2][i]==board[j+3][i]==board[j+4][i]=='O':
        print('you win')
        return True
      if board[i][j]==board[i][j+1]==board[i][j+2]==board[i][j+3]==board[i][j+4]=='X':
        print('you loss')
        return True
      if board[j][i]==board[j+1][i]==board[j+2][i]==board[j+3][i]==board[j+4][i]=='X':
        print('you loss')
        return True
  for i in range(6):
    for j in range(6):
      if board[i][j]==board[i+1][j+1]==board[i+2][j+2]==board[i+3][j+3]==board[i+4][j+4]=='O':
        print('you win')
        return True
      if board[i][j+4]==board[i+1][j+3]==board[i+2][j+2]==board[i+3][j+1]==board[i+4][j]=='O':
        print('you win')
        return True
      if board[i][j]==board[i+1][j+1]==board[i+2][j+2]==board[i+3][j+3]==board[i+4][j+4]=='X':
        print('you loss')
        return True
      if board[i][j+4]==board[i+1][j+3]==board[i+2][j+2]==board[i+3][j+1]==board[i+4][j]=='X':
        print('you loss')
        return True

def end(board):
  empty = [[i, j] for i in range(10) for j in range(10) if board[i][j] == '.']
  if empty==[]:
    print('end')
    return True
  else:
    return False

def main():
  list1 = create()

  while True:
    computer(list1)
    see(list1)
    if win_loss(list1):
      break
    if end(list1):
      break
    
    user(list1)
    see(list1)
    if win_loss(list1):
      break
    if end(list1):
      break

main()