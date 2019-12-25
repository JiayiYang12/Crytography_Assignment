P = input('请输入英文句子：')
keys = input('请输入密钥（大写字母构成）：')

L = len(P)

# 将明文转换为0 - 26的数字，所得的数字表
N_C = [ord(c) - 97 for c in P]

# 将密钥转换为数字串
N_keys = [ord(c) - 65 for c in keys]
print('密钥数字串: {0}'.format(N_keys))

# 构造与明文对应的密钥
K = []
Int_ = L // len(keys)
Remain = L % len(keys)
K = N_keys * Int_
for i in range(Remain):
	K.append(N_keys[i])

print('与明文相对应的密钥数字串: {0}'.format(K))

# 对明文加密
C = []
for i in range(L):
	C.append(chr((N_C[i]+ K[i]) % 26 + 65))
	
print('密文：{0}'.format(''.join(C)))

# 解密，即将密文再转换为明文
de_C = []
for i in range(L):
	de_C.append(chr(((ord(C[i]) - 65) - K[i]) % 26 + 97))
	
print('由密文转换为明文：{0}'.format(''.join(de_C)))