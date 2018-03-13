"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
	my_program tcp <host> <port> [--timeout=<seconds>]
	my_program serial <port> [--baud=<n>] [--timeout=<seconds>]
	my_program (-i | --interactive)
	my_program (-h | --help | --version)
Options:
	-i, --interactive  Interactive Mode
	-h, --help  Show this screen and exit.
	--baud=<n>  Baudrate [default: 9600]
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from MyDecoration import docopt_cmd


class PromptCmd(cmd.Cmd):
	file = None

	@docopt_cmd
	def do_tcp(self, arg):
		"""Usage: tcp <host> <port> [--timeout=<seconds>]"""

		print(arg)

	@docopt_cmd
	def do_serial(self, arg):
		"""Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
	--baud=<n>  Baudrate [default: 9600]
		"""

		print(arg)

	def do_quit(self, arg):
		"""Quits out of Interactive Mode."""

		print('Good Bye!')
		exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
	prompt = PromptCmd()
	prompt.intro = 'Caesar Cypher Tool'+'\n=================='
	prompt.prompt = '\n> '
	prompt.cmdloop()('Starting...')
print(opt)
