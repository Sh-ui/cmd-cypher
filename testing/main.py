"""
Usage:
  cypher.py encrypt (-t|-f) IN [SHFT] [PATH] [-o]
  cypher.py decrypt (-t|-f) IN [SHFT [PATH] | ((-a) PATH)] [-o]
  cypher.py (-? | -h | --help)
  cypher.py (-q | -quit)
  cypher.py (-i | --interactive)
Options:
  -t, --text         type a string as a input
  -f, --file         give a file as input
  -i, --interactive  Interactive Mode
  -h, --help         show this screen and exit.
  -o, --override     re-write input file
  -a, --auto         write all shift attempts to file
  SHFT         character shift amount [default:3]
  PATH         path out directory [default:cypherOUT.txt]
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from MyDecoration import docopt_cmd
from funcs import *

SHFT = 3

class PromptCmd(cmd.Cmd):
	file = None

	def do_quit(self, arg):
		'''exits the app.'''
		print('exiting...')
		exit()

	@docopt_cmd
	def do_encrypt(self, arg):
		'''Usage: encrypt (-t|-f) IN [SHFT] [PATH] [-o]'''
		if arg['IN'] != None and -t == True:
			text = del_punc(arg['IN'])
			shft = SHFT if arg['SHFT'] == None else int(arg['SHFT'])
			encrypted = cypher(text,shift)
			print('\n ',encrypted.upper())

	@docopt_cmd
	def do_decrypt(self, arg):
		'''Usage: decrypt (IN | -f FILE) [SHFT [PATH] | ((-a) PATH)] [-o]'''
		text = del_punc(arg['IN'])
		shift = int(arg['PATH'])
		encrypted = cypher(text,shift)
		print('\n ',encrypted.upper())


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
	prompt = PromptCmd()
	prompt.intro = 'Caesar Cypher Tool\n'+('='*18)
	prompt.prompt = '\n> '
	prompt.cmdloop()('Starting...')

print(opt)
