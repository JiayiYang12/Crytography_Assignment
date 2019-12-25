a, b = input('请输入两个均不为零的自然数（用逗号隔开）：').split(',')
a, b = int(a), int(b)
x = 1;
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
print('运用扩展欧几里得算法的结果为：')
print(g, x, y)
print('{0}为{1}在模{2}下的乘法逆元'.format(y, b, a))

