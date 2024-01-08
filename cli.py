# cli.py

import sys
if sys.version_info.major < 3:
  raise Exception('only support python v3+')

import os, traceback

from dapp_lib.pyexp import *

def cli_loop():
  print('input script and press ENTER to run, input "break" to quit.\n')
  
  ns = {'var':{}}
  
  while True:
    s = input('> ').strip()
    if not s: continue
    if s == 'break': break
    
    try:
      print('%r' % pyexp(s,ns))
    except:
      traceback.print_exc()
  
  print('\nPyExp command loop finished!\n')


if __name__ == '__main__':
  cli_loop()

# usage:
#   python3 -i cli.py
