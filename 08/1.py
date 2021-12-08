def count_lengths(strings, lengths):
  count = 0
  for string in strings:
    if len(string) in lengths:
      count += 1
  return count

file = open("input.txt", "r")

signals = []
outputs = []

for line in file:
  line = line.rstrip()
  line = line.split(" | ")

  signal = line[0]
  output = line[1]

  signal = signal.split(" ")
  output = output.split(" ")

  signals.append(signal)
  outputs.append(output)


#total = signals + outputs
targets = [2, 4, 3, 7]
total_count = 0
for entry in outputs:
  c = count_lengths(entry, targets)
  total_count += c

print(total_count)
