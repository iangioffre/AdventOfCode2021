#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 1, Problem 1
"""

import sys

def main():
  filename = sys.argv[-1]
  if filename == __file__:
    print('This program requires an input file')
    return

  infile = open(filename, 'r')
  inputs = infile.readlines()
  inputs = [int(input.strip()) for input in inputs]
  infile.close()
  
  total = 0
  lastInput = inputs[0]
  for input in inputs[1:]:
    if input > lastInput:
      total += 1
    lastInput = input

  print(total)


if __name__ == '__main__':
  main()