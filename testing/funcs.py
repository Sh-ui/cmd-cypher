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
