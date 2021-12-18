def find_number()

def check_explode(i, line):
  while line[i] != "[":
    i += 1
    if line[i] == "]":
      return

  stop = find_closing(line, i) 
  sub = line[i + 1:stop + 1]
  sub = sub.strip("[]")
  sub = sub.split(", ")

  print(sub)
  quit()
    

def find_closing(line, s):
  i = s
  while line[i] != "]":
    i += 1
  return i

def snail_reduce(line):
  depth = 0
  while(True):
    for i in range(len(line)):
      if line[i] == '[':
        depth += 1
      elif line[i] == ']':
        depth -= 1
      if depth == 4:
        check_explode(i, line)



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
  line = str(line)

  snail_reduce(line)