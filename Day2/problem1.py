#!/usr/bin/env python3

"""
  Advent of Code 2021
  Day 2, Problem 1
"""

import sys

def main():
  filename = sys.argv[-1]
  if filename == __file__:
    print('This program requires an input file')
    return

  infile = open(filename, 'r')
  inputs = infile.readlines()
  inputs = [input.strip().split() for input in inputs]
  infile.close()
  
  hpos = 0
  vpos = 0

  for input in inputs:
    direction = input[0]
    speed = int(input[1])
    if (direction == 'forward'):
      hpos += speed
    elif (direction == 'up'):
      vpos -= speed
    elif (direction == 'down'):
      vpos += speed

  location = hpos * vpos
  print(location)


if __name__ == '__main__':
  main()