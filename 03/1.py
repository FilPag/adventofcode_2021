lines = open("input.txt", "r")
inputs = []

for l in lines:
  inputs.append(l[:-1])

counts = []
#prep counts
for i in range(len(inputs[0])):
  counts.append((0, 0))

for data in inputs:
  for i in range(len(data)):
    if data[i] == '0':
      counts[i] = (counts[i][0] + 1, counts[i][1])
    else:
      counts[i] = (counts[i][0], counts[i][1] + 1)

gamma = ""
epsilon = ""
#counts.reverse()

for c in counts:
  if c[0] > c[1]:
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'

print(counts)
print(gamma)
print(epsilon)

prod = int(gamma, 2) * int(epsilon, 2)

print(prod)