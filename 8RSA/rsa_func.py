import random

def gcd(a, b):
	'''
	求最大公约数
	'''
	if b > a:
		a, b = b, a
	if b == 0:
		return a
	else: 
		return gcd(b, a % b)

def exte_gcd(a, b):
	x = 1;
	y = 0;
	y = 0;
	g = a;
	r = 0;
	s = 1;
	t = b;
	u = 0;
	v = 0;
	w = 0;
	while t > 0:
		q = g // t;
		u = x - q*r; v = y - q*s; w = g - q*t;
		x = r; y = s; g = t;
		r = u; s = v; t = w;
	if y < 0:
		y = y + a
		x = x + 1
	return y
	
	
def gen_e(n, fi_n):
	ls = []
	for i in range(2, fi_n):
		if gcd(i, fi_n) == 1:
			ls.append(i)
	return random.choice(ls)

def gen_key(p, q):
	'''
	生成密钥
	Returns:
		[n, e]: 公钥
		[n, d]: 密钥
	'''
	n = p * q
	fi_n = (p-1) * (q-1)
	e = gen_e(n, fi_n)
	d = exte_gcd(fi_n, e)
	return [n, e], [n, d]

def encode(m, k):
	n = k[0]
	e = k[1]
	y = pow(m, e) % n
	return y

def decode(c, k):
	n = k[0]
	d = k[1]
	y = pow(c, d) % n
	return y

