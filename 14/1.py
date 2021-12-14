def step(seq, pairs):
  new_seq = ""
  prev = seq[0]
  for c in seq[1:]:
    new_seq += prev
    p = prev + c
    if p in pairs:
      new_seq += pairs[p]
    prev = c
  new_seq += seq[-1]
  return new_seq

def count_occurence(seq):
  counts = {}
  for c in seq:
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1
  return counts
  
if __name__ == "__main__":
  STEPS = 10
  file = open("input.txt")
  sequence = file.readline().rstrip()
  file.readline() #Empty line skip

  pairs = {}
  line = file.readline()
  while line != "":
    line = line.rstrip()
    line = line.split(" -> ")
    a, b = line
    pairs[a] = b
    line = file.readline()
  
  for i in range(STEPS):
    sequence = step(sequence, pairs)
  
  counts = count_occurence(sequence)
  max_c = max(counts.values())
  min_c = min(counts.values())
  print(max_c - min_c)
