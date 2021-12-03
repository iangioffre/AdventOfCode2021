#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 3, Problem 1
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
  
  gamma = ''
  epsilon = ''

  maxlength = len(max(inputs, key=len))

  for i in range(-maxlength, 0):
    input_digits = []
    for input in inputs:
      try:
        input_digits.append(int(input[i]))
      except IndexError:
        input_digits.append(0)
    mcb = max(input_digits, key=input_digits.count)
    gamma += str(mcb)
    epsilon += str( (int(mcb) + 1) % 2 )
    

  consumption = int(gamma, 2) * int(epsilon, 2)
  print(consumption)


if __name__ == '__main__':
  main()