import random
P = input('请输入待解密的英文句子：')

# 大写、小写字母表
low_keys = 'abcdefghijklmnopqrstuvwxyz'
up_keys = ''.join([chr(ord(c) - 32) for c in low_keys])

# 构建置换关系
d = {}
rep_list = []
for c in up_keys:
	while True:
		tmp = random.choice(low_keys)
		if tmp not in rep_list:
			rep_list.append(tmp)
			break			
	d[c] = tmp

# 解密
de_C = [d[c] for c in P]
print('由密文转换为明文：{0}'.format(''.join(de_C)))