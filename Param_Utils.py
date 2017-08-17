import string
import re
import base64

def __b32enc(dec):
	dec = str(dec)
	enc = base64.b32encode(dec)
	enc = enc.replace('=','')
	enc = enc.lower()
	return enc

def __b32dec(enc):
	enc = str(enc)
	while len(enc) % 8 != 0:
		enc += '='
	enc = enc.upper()
	return base64.b32decode(enc)

#seed sanitize
def __ss(seed):
	return re.sub('[^' + string.ascii_letters + string.digits + ']', '', str(seed))
def sanitize_seed(seed):
	return __ss(seed)
	
#number sanitize
def __ns(i):
	return str(int(i))

def decode(encoded):
	l = __b32dec(encoded)
	l = l.split('|')
	return (int(l[0]), int(l[1]), int(l[2]), l[3])

def encode(xd, yd, sp, seed):
	l = [__ns(xd), __ns(yd), __ns(sp),__ss(seed)]
	l = "|".join(l)
	return __b32enc(l)
	
def encode_format(encoded):
	l = params_decode(encoded)
	return param_format(l[0], l[1], l[2], l[3])

def param_format(xd, yd, sp, seed):
	xd = __ns(xd)
	yd = __ns(yd)
	sp = __ns(sp)
	seed =__ss(seed)
	
	out = "Maze Hash: " + encode(xd, yd, sp, seed) + "\n"
	out += "Dimensions: " + xd + "x" + yd + "\n"
	out += "Mutations: " + sp
	return out
	
	