from os import system, name

def updatescreen(lines):
  system('cls' if name == 'nt' else 'clear')
  d = ''
  for i in range(66):
      d = d + '█'
  print(d)
  for i in lines:
    print(f'█{i}█')
  print(d)

class editablelist:
  def __init__(self, list):
    self.list = list



def setstartscreen(list):
  d =  ''
  for i in range(24):
    d = ''
    for i in range(64):
      d = d + '⠀'
      #d = d + '/'
    list.list.append(d)

class component:
  def __init__(self, x, y, width, height, screen):
    for xi in range(height):
      line = screen.list[y + xi]
      objstr = ''
      for i in range(width):
        objstr = f'{objstr}█'
      screen.list[y + xi] = f'{line[:x]}{objstr}{line[(x + width):]}'

class picture:
  def __init__(self, x, y, picture, screen):
    for xi in range(len(picture)):
      line = screen.list[y + xi]
      objstr = picture[xi]
      width = len(objstr)
      screen.list[y + xi] = f'{line[:x]}{objstr}{line[(x + width):]}'

class strtopic:
  def __init__(self, picture):
    self.picture = picture.split('\n')
      
    
