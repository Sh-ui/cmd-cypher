"""
Usage:
  cypher.py encrypt [-w][-o DIR]([-r|-s CHR][-m N])(-t IN...|-f IN...)
  cypher.py decrypt [-w][-o DIR][-s CHR|-a](-t IN...|-f IN...)
  cypher.py -i
  cypher.py -h
  cypher.py -q

Options:
  -w --overwrite  
  -o DIR --output=DIR  [default: cyphOUT.txt]
  -s CHR --shift=CHR   type a single number or #-#.. to vary
  -r RNG --random RNG  single number as max or #min-#max..
  -m N --move=N        shift or randomize every N characters
  -a --auto        test all shift attempts and write to file
  -t --text
  -f --file
  -i --interactive
  -?, -h, --help
  -q --quit
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
