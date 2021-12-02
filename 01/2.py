from collections import deque
lines = open("input1.txt", "r")

prev = []
current = deque(maxlen = 3)
counter = 0

for c in lines:
  current.append(int(c))
  if len(prev) == 3:
    if sum(current) > sum(prev):
      counter += 1
  prev = current.copy()

print(counter)