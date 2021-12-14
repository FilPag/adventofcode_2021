from collections import defaultdict
def step(pair_counts, letter_counts, pairs): 
  updated = pair_counts.copy()
  keys = list(pair_counts.keys())
  for pair in keys:
    a, b = pair
    letter = pairs[pair]
    no_new = pair_counts[pair]

    letter_counts[letter] += no_new
    updated[a + letter] += no_new
    updated[letter + b] += no_new
    updated[pair] -= no_new

  return updated

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
  
  letter_counts = defaultdict(lambda: 0)
  pair_counts = defaultdict(lambda: 0)

  prev = sequence[0]
  letter_counts[prev] += 1
  for c in sequence[1:]:
    letter_counts[c] += 1
    pair_counts[prev + c] += 1
    prev = c

  for i in range(40):
    pair_counts = step(pair_counts, letter_counts, pairs)

  max_c = max(letter_counts.values())
  min_c = min(letter_counts.values())
  print(max_c - min_c)
