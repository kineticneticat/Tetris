import time
from random import randint

clear = lambda: print("\033c", end="")

unicode = {
  'back' : '⬛',
  'red' : '🟥'
}

board = [
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],
  ['back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', '\n'],  
]

pieces = {
}

class tetronimo:
  def __init__(self, shape, x, y, rot, set):
    self.shape = shape #shape of the peice (t l etc.)
    self.x = x # 0 - 9 | x of the centre
    self.y = y # 0 - 19 | y of the centre
    self.rot = rot # 0, 90, 180, 270 | roataion of the piece
    self.set = set # bool | is the piece finished falling
  
  def add(self):
    board[self.y][self.x] = 'red'
  
  def down(self):
    if not self.set:
      if self.y == 19:
        self.set = True
        pass
      else:
        board[self.y][self.x] = 'back'
        board[self.y + 1][self.x] = 'red'
        self.y += 1

  def right(self):
    if not self.set:
      if self.x == 9:
        pass
      else:
        board[self.y][self.x] = 'back'
        board[self.y][self.x + 1] = 'red'
        self.x += 1

  def left(self):
    if not self.set:
      if self.x == 0:
        pass
      else:
        board[self.y][self.x] = 'back'
        board[self.y][self.x - 1] = 'red'
        self.x -= 1


def draw():
  for i in board:
    for j in i:
      try:
        print(unicode[j], end='')
      except KeyError:
        print(j, end='')

def tick():
  time.sleep(1)
  clear()
  draw()
  print(shapelist[blocks[0]].y)

def controls(input):
  if input == 'a':
    shapelist['testshape'].left()
  elif input == 'd':
    shapelist['testshape'].right()
  
shapelist = {}
blocks = ['', '', '', '']
for i in range(len(blocks)):
  blocks[i] = randint(0, 9)

for i in range(len(blocks)):
  shapelist[str(i)] = tetronimo('dot', 5, 0, 0, False)
  shapelist[str(i)].add()

while 1 != 0:
  tick()
  #moving
  controls(str(input()))
  shapelist['testshape'].down()
