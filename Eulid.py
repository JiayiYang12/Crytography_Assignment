a_, b_ = input('请输入两个均不为零的自然数（用逗号隔开）：').split(',')
a, b = int(a_), int(b_)
while b > 0:
	r = a % b
	a = b
	b = r

res = a
print('{}和{}的最大公约数为{}'.format(a_, b_, res))