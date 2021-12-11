
def get_closing_for(c):
  counter_parts = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
    }
  
  return counter_parts[c]

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


if __name__ == "__main__":
  file = open("input.txt", "r")

  score_table = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
  }
  score = 0
  for line in file:
    line = line.rstrip()
    error = check_unexpected(line)
    if error:
      score += score_table[error]

  print(score)