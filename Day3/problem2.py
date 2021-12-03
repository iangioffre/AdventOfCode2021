#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 3, Problem 2
"""

import sys

def main():
  filename = sys.argv[-1]
  if filename == __file__:
    print('This program requires an input file')
    return

  infile = open(filename, 'r')
  inputs = infile.readlines()
  inputs = [input.strip() for input in inputs]
  infile.close()
  
  w_oxygen = ''
  w_co2 = ''
  oxygen = 0
  co2 = 0

  maxlength = len(max(inputs, key=len))

  for i in range(-maxlength, 1):
    oxygen_digits = [1, 0] # trick max into picking 1 if same
    co2_digits = [0, 1] # trick min into picking 0 if same
    newinputs = inputs.copy()
    for input in inputs:
      try:
        idx = i if i != 0 else len(input)
        if input[:idx] == w_oxygen:
          oxygen_digits.append(int(input[i]))
          if len(oxygen_digits) == 3:
            oxygen = input
        if input[:idx] == w_co2:
          co2_digits.append(int(input[i]))
          if len(co2_digits) == 3:
            co2 = input
        if input[:idx] != w_oxygen and input[:idx] != w_co2:
          newinputs.pop(newinputs.index(input))
      except IndexError:
        oxygen_digits.append(0)
        co2_digits.append(0)
    if len(oxygen_digits) == 3 and len(co2_digits) == 3:
      break
    inputs = newinputs.copy()
    mcb = max(oxygen_digits, key=oxygen_digits.count)
    lcb = min(co2_digits, key=co2_digits.count)
    w_oxygen += str(mcb)
    w_co2 += str(lcb)
    
  consumption = int(oxygen, 2) * int(co2, 2)
  print(consumption)

if __name__ == '__main__':
  main()