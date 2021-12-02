lines = open("input1.txt", "r")

prev = 0
counter = 0
for i, c in enumerate(lines):
  if i != 0 and int(c) > prev:
    counter += 1
  prev = int(c)

print(counter)