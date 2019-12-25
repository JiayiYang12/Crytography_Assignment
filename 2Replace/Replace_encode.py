import random
P = input('请输入英文句子：')

# 大写、小写字母表
low_keys = 'abcdefghijklmnopqrstuvwxyz'
up_keys = ''.join([chr(ord(c) - 32) for c in low_keys])

# 构建置换关系
d = {}
rep_list = []
for c in low_keys:
	while True:
		tmp = random.choice(up_keys)
		if tmp not in rep_list:
			rep_list.append(tmp)
			break			
	d[c] = tmp

print('置换关系：')
print(d)

# 对明文进行加密
C = [d[c] for c in P]
print('密文：{0}'.format(''.join(C)))

# 构建解密置换关系，即将置换关系的键和值互换
rev_d = {v: k for k, v in d.items()}

# 解密，即将密文再转换为明文
de_C = [rev_d[c] for c in C]
print('由密文转换为明文：{0}'.format(''.join(de_C)))

