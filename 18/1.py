import math

def modify_list(target, value):
  if target is not None:
    l, i = target
    l[i] = value

def split(number):
 left = int(number // 2) 
 right = int(math.ceil(number / 2))
 return [left, right]

def explode(line, left, right):
  modify_list(left, line[0])
  modify_list(right, line[1])
  return 0

def snail_reduce(line, left, right, nesting):
  if line[0] == [8, 4]:
    print(nesting)

  if nesting == 4:
    if isinstance(line[0], list):
      line[0] = explode(line[0], left, (line, 1))
    elif isinstance(line[1], list):
      line[1] = explode(line[1], (line, 0), right)

  if isinstance(line[0], int) and line[0] >= 10:
    line[0] = split(line[0])
  elif isinstance(line[0], list):
    snail_reduce(line[0], (line, 0), right, nesting + 1)
  
  if isinstance(line[1], int) and line[1] >= 10:
    line[1] = split(line[0])
  elif isinstance(line[1], list):
    snail_reduce(line[1], left, (line, 1), nesting + 1)
  
if __name__ == "__main__":
  '''
  file = open('input.txt')
  assignment = []
  for line in file:
    l = json.loads(line)
    assignment.append(l)
  
  file.close()
  '''

  line = [[[[4,3],4],4],[7,[[8,4],9]]]
  line = [line, [1, 1]]

  snail_reduce(line, None, None, 1)
  print(line)