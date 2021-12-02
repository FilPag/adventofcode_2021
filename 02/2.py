lines = open("input.txt", "r")
h = 0
v = 0
aim = 0
for c in lines:
  command = c.split(" ")
  match command[0]:
    case "forward":
      h += int(command[1])
      v += aim * int(command[1])
    case "down":
      aim += int(command[1])
    case "up":
      aim -= int(command[1])

print(v)
print(h)
print(v * h)