#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 1, Problem 2
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
  lastSum = sum(inputs[0:3])
  for i, nextInput in enumerate(inputs[3:]):
    nextSum = lastSum - inputs[i] + nextInput
    if nextSum > lastSum:
      total += 1
    lastSum = nextSum

  print(total)


if __name__ == '__main__':
  main()