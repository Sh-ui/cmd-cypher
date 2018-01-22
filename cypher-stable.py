import cmd

def sym_extract(text,syms):
	text = text[text.find(syms[0])+1:text.find(syms[1])]
	return text

def del_punc(string):
	string = ''.join(ch if ch.isalnum() else '' if ch!=' ' else ' ' for ch in string)
	return(string.lower())

def cypher(text, shift):
	text = del_punc(text)
	secret = ''
	for c in text:
		if c in 'abcdefghijklmnopqrstuvwxyz':
			num = ord(c)
			num += shift
			if num > ord('z'):
				num -= 26
			elif num < ord('a'):
				num += 26
			secret = secret + chr(num)
		else:
			secret = secret + c
	return secret


class CryptoPromptCmd(cmd.Cmd):
	prompt = '\n> '

	def default(self, arg):
		print('invalid command, try typing "help"')

	def do_quit(self, arg):
		'''exits the program'''
		return True

	def do_encrypt(self, arg):
		'''usage: encrypt (provided string or /filename)[shift number]'''
		if arg != '':
			text  = del_punc(sym_extract(arg,'()'))
			shift = int(sym_extract(arg,'[]'))
			encrypted = cypher(text,shift)
			print('\n ',encrypted.upper())
		else:
			print('invalid command\nusage: encrypt(provided string or /filename)[shift number]')
			return

	def do_decrypt(self, arg):
		'''usage:\noutput to file: decrypt(provided string or /filename)[file]\nattempt manually: decrypt(provided string or /filename)[shift number]'''
		if arg != '':
			text  = del_punc(sym_extract(arg,'()'))
			shift = -1*int(sym_extract(arg,'[]'))
			decrypted = cypher(text,shift)
			print('\n ',decrypted.upper())
		else:
			print('invalid command\nusage:')
			print('output to file: decrypt(provided string or /filename)[output /filename]')
			print('attempt manually: decrypt(provided string or /filename)[shift number]')
			return


if __name__ == '__main__':
	print('\n'* 3)
	print("Ian's Caesar Cypher Tool")
	print('========================')
	print()
	print('type "help" for commands')
	print()
	CryptoPromptCmd().cmdloop()
	print('\nexiting...\n')
