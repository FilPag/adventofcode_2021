def count_occurence(inputs, i):
  zero = 0 
  one = 0
  for s in inputs:
    if s[i] == '0':
      zero += 1
    else:
      one += 1
  return (zero, one)

def find_all_with(inputs, target, index):
  res = []
  for row in inputs:
      if row[index] == target:
        res.append(row)
  return res

def find_o2_rating(inputs):
  index = 0
  prev = []
  while len(inputs) > 1:
    count = count_occurence(inputs, index)
    target = ''
    if count[0] == count[1]:
      target = '1'
    elif count[0] > count[1]:
      target = '0'
    else:
      target = '1'

    prev = find_all_with(inputs, target, index)
    index +=1
    inputs = prev.copy()
  return inputs[0]

def find_co2_rating(inputs):
  index = 0
  prev = []
  while len(inputs) > 1:
    count = count_occurence(inputs, index)
    target = ''
    if count[0] == count[1]:
      target = '0'
    elif count[0] < count[1]:
      target = '0'
    else:
      target = '1'

    prev = find_all_with(inputs, target, index)
    index +=1
    inputs = prev.copy()
  return inputs[0]

lines = open("input.txt", "r")
inputs = []
for l in lines:
  inputs.append(l[:-1])

o2_rating = find_o2_rating(inputs)
co2_rating = find_co2_rating(inputs)

print(o2_rating)
print(co2_rating)

o2_rating = int(o2_rating, 2)
co2_rating = int(co2_rating, 2)
    
print(o2_rating)
print(co2_rating)

print(o2_rating * co2_rating)
