#!/usr/bin/python3


import sys
import readchar


cells_pntr = 0
cells = [ 0 ]
loop_starts = []
str_pntr = 0

try:
  str = open(sys.argv[1], 'r').read()
except IndexError:
  print('Error: Requires bf file')
  exit()
except FileNotFoundError:
  print('Error: File nonexistent')
  exit()


while str_pntr < len(str):
  char = str[str_pntr]

  if not char:
    break
  else:
    if char == '>':
      cells_pntr = cells_pntr + 1
      if cells_pntr > len(cells)-1: cells.append(0)
    if char == '<':
      cells_pntr = cells_pntr - 1
      if cells_pntr < 0: cells_pntr = len(cells)
    if char == '+': cells[cells_pntr] = cells[cells_pntr]+1
    if char == '-': cells[cells_pntr] = cells[cells_pntr]-1
    if char == '.': print(chr(cells[cells_pntr]))
    if char == ',': cells[cells_pntr] = ord(readchar.readchar())
    if char == '[': loop_starts.append(str_pntr)
    if char == ']':
      if cells[cells_pntr] == 0:loop_starts.pop(-1)
      else:str_pntr = loop_starts[-1]

  str_pntr = str_pntr+1
