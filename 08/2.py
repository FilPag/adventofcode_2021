def add_char_count(source, target, mapping):
  for c in source:
    for c2 in target:
      mapping[c][c2] += 1

def process_signal_base(signal,mapping):
  signal = sorted(signal)
  signal = "".join(signal)

  match len(signal):
    case 2:
      mapping[1] = signal
    case 3:
      mapping[7] = signal
    case 4:
      mapping[4] = signal
    case 7:
      mapping[8] = signal

def get_overlap(s1, s2):
  return [c for c in s1 if c in s2]

def check_substring(s1, s2):
  for c in s1:
    if c not in s2:
      return False

  return True

def process_signal_rest(signal, mapping):
  signal = sorted(signal)
  signal = "".join(signal)

  if len(signal) == 5:
    if check_substring(mapping[1], signal):
      mapping[3] = signal
    elif len(get_overlap(signal, mapping[4])) == 3:
      mapping[5] = signal
    else:
      mapping[2] = signal
  elif len(signal) == 6:
    if check_substring(mapping[4], signal):
      mapping[9] = signal
    elif len(get_overlap(signal, mapping[1])) == 2:
      mapping[0] = signal
    else:
      mapping[6] = signal
      
    
def decode_signal(signal, mapping):
  for part in signal:
    process_signal_base(part, mapping)

  for part in signal:
    process_signal_rest(part, mapping)

def get_output(output, mapping):
  string = ""
  for part in output:
    part = sorted(part)
    part = "".join(part)
    num = mapping.index(part) 
    string += str(num)

  return int(string)
  


  
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
mapping = ["" for _ in range(10)]
csum = 0
for i in range(len(signals)):
  decode_signal(signals[i], mapping)
  csum += get_output(outputs[i], mapping)

print(csum)

