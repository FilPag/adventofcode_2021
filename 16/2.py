import math
def read_literal(sequence):
  value , sequence= trim_n_bits(sequence, 5)
  leading = value[0]
  value = value[1:]

  while leading != "0":
    next_group, sequence = trim_n_bits(sequence, 5)
    leading = next_group[0]
    next_group = next_group[1:]
    value += next_group
  
  return int(value, base=2), sequence


def trim_n_bits(sequence, n):
  trim =  sequence[:n]
  sequence =  sequence[n:]
  return trim, sequence

def read_header(sequence):
  version, sequence = trim_n_bits(sequence, 3)
  type_id, sequence = trim_n_bits(sequence, 3)
  
  version = int(version, base=2)
  type_id= int(type_id, base=2)
  return version, type_id, sequence

def expand_char(c):
  int_value = int(c, base=16)
  string = str(bin(int_value))[2:]
  return string.zfill(4)

def process_sub(mode, sequence):
  values = []
  if mode == '0':
      no_bits, sequence = trim_n_bits(sequence, 15)
      no_bits = int(no_bits, base=2)
      subs, sequence = trim_n_bits(sequence, no_bits)
      while subs != "":
        sub_v, subs = process_packet(subs)
        values.append(sub_v)
  else:
    no_packets, sequence = trim_n_bits(sequence, 11)
    no_packets = int(no_packets, base=2)
    for _ in range(no_packets):
      sub_v, sequence = process_packet(sequence)
      values.append(sub_v)
  return values, sequence

def process_packet(sequence):
  _, tid, sequence =  read_header(sequence)
  if tid == 4:
    return read_literal(sequence)

  mode, sequence = trim_n_bits(sequence, 1)
  res = 0
  vals, seq = process_sub(mode, sequence)
  match tid:
    case 0:
      res = sum(vals)
    case 1:
      res = math.prod(vals)
    case 2:
      res = min(vals)
    case 3:
      res = max(vals)
    case 5:
      if vals[0] > vals[1]:
        res = 1
      else:
        res = 0
    case 6:
      if vals[0] < vals[1]:
        res = 1
      else:
        res = 0
    case 7:
      if vals[0] == vals[1]:
        res = 1
      else:
        res = 0
  return res, seq

if __name__ == "__main__":
  file = open("input.txt", "r")

  sequence = ""
  line = file.readline().rstrip()
  file.close()
  for c in line:
    sequence += expand_char(c)
  
  
  tot_value = process_packet(sequence)[0]
  print(tot_value)