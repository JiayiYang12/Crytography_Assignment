from rsa_func import *

m = int(input('请输入一个整数作为明文：'))
p, q = input('请输入两个大素数（用逗号隔开）：').split(',')
p, q = int(p), int(q)

# 生成密钥
K_p, K_c = gen_key(p, q)
c = encode(m, K_p)
m = decode(c, K_c)
print('加密后的密文：{0}; 解密后的明文：{1}'.format(c, m))