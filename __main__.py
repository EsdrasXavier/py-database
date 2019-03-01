#!/usr/bin/python3
import sys
sys.path.insert(0, 'PyDatabase/')

import Constants
from PyDatabase import PyDatabase

if __name__ == '__main__':
  try:
    db = PyDatabase()
    db.run()
  except KeyboardInterrupt:
    print("\nPressed CTRL+C... Killing")
  except EOFError:
    print("{}Bye".format(Constants.BOLD))