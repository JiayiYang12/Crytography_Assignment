n = int(input('请输入一个整数：'))
sq_n = pow(n, 0.5)
m = n
p = 2
while p <= sq_n:
	if m % p == 0:
		print('{0}是合数，且{1}是它的的因子'.format(p, int(m)))
		m //= p
	else:
		p += 1

if m == n:
	print('{0}是素数'.format(n))
elif m > 1:
	print('{}的最后一个质数是{}'.format(n, m))
	