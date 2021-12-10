def get_closing_for(c):
  counter_parts = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
    }
  
  return counter_parts[c]

def get_autocomplete(line):
  openers = ["(", "[", "{", "<"]
  expected_closing = []

  for c in line:
    if c in openers:
      closer = get_closing_for(c)
      expected_closing.insert(0, closer)
    else:
      expected_closing.pop(0)
  
  return expected_closing


def check_unexpected(line):
  openers = ["(", "[", "{", "<"]
  expected_closing = []

  for c in line:
    if c in openers:
      closer = get_closing_for(c)
      expected_closing.append(closer)
    else:
      expected = expected_closing.pop(-1)
      if expected != c:
        return c

file = open("input.txt", "r")

score_table = {
  ")" : 1,
  "]" : 2,
  "}" : 3,
  ">" : 4,
}
incomplete = []
for line in file:
  line = line.rstrip()
  error = check_unexpected(line)
  if not error:
    incomplete.append(line)

scores = []
for line in incomplete:
  auto_complete = get_autocomplete(line)
  score = 0
  for c in auto_complete:
    score *= 5
    score += score_table[c]
  scores.append(score)

scores = sorted(scores)
middle = int((len(scores) - 1) / 2)

middle = scores[middle]

print(middle)
