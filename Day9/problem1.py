#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 9, Problem 1
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
  
  risk_levels = []

  for row in range(len(inputs)):
    for col in range(len(inputs[row])):
      if row - 1 >= 0 and inputs[row-1][col] <= inputs[row][col]:
        continue 
      if row + 1 < len(inputs) and inputs[row+1][col] <= inputs[row][col]:
        continue 
      if col - 1 >= 0 and inputs[row][col-1] <= inputs[row][col]:
        continue 
      if col + 1 < len(inputs[row]) and inputs[row][col+1] <= inputs[row][col]:
        continue 
      risk_levels.append(int(inputs[row][col]) + 1)

  sum_of_risk = sum(risk_levels)
  print(sum_of_risk)


if __name__ == '__main__':
  main()