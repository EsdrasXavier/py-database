#!/usr/bin/python3

__version__ = '1.0.0'
__author__ = 'Esdras Xavier Raimundo'
__license__ = 'GNU'
__email__ = 'esdrasxa@gmail.com'
__github__ = 'https://github.com/EsdrasXavier/py-database'


import Constants
import itertools
from helpers import compare

class PyDatabase(object):

  commands = ['new', 'database', 'info', 'show']

  def __init__(self, *args, **kwargs):
    self.__db = '(none)'
    self.welcolme()
    self.__run = True


  def welcolme(self):
    text = 'PyDatabase. A database builded in python\n' \
           'Version: {}\n' \
           'Made by: {}\n' \
           '         {}\n'.format(__version__, __author__, __email__)

    print("{}{}{}".format(Constants.BOLD, text, Constants.END))


  def info(self):
    text = 'Welcolme to the PyDatabase. A database builded in python\n' \
           'Version: {}\n' \
           'Made by: {}\n' \
           '         {}\n' \
           '         {}\n'.format(__version__, __author__, __email__, __github__)

    print("\n{}{}{}".format(Constants.BOLD, text, Constants.END))


  def run(self):
    while self.__run:
      command = raw_input("PyDatabase [{}]> ".format(self.__db)).lower()
      self.command_handler(command)


  def command_handler(self, command):

    if 'exit' in command:
      self.__run = False
      raise EOFError

    if self.check_for_error(command):
      return

    command = command.replace(';', '').split(' ')

    print(command)

    if 'new' == command[0]:
      print('a')
    elif 'show' in command and 'info' in command:
      self.info()



  def check_for_error(self, command):
    '''Will verify for errors
    '''
    # Check if has a command
    if len(command) < 1:
      self.print_error('No query specified.')
      return True

    # Check if has a semi-colon in the final of the query
    elif command[-1::] is not ';':
      self.print_error("You must put a ';' in the final of the query")
      return True

    # Check if the command exists
    else:
      command = command.split(' ')
      if command[0] not in self.commands:
        self.print_error('Command not found')
        return True

    return False



  def print_error(self, error):
    print('ERROR: {}\n'.format(error))