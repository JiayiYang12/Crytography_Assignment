P = input('请输入英文句子：')
K = int(input('请输入移位密码的密钥：'))
L = len(P)
N_C = []
A_C = []
N_C_rev = []
N_C1 = []
C = []


# keys = 'abcdefghijklmnopqrstuvwxyz'
# 将明文转换为0 - 26的数字，所得的数字表
N_C = [ord(c) - 97 for c in P]

# 对明文进行加密，所得的加密数字表
N_C1 = [(n + K) % 26 for n in N_C]
	
# 得到密文
A_C = [chr(n + 97) for n in N_C1]
print('密文：{0}'.format(''.join(A_C)))

# 将密文再转换为明文
N_C_rev = [chr((N_C1[i] - K) % 26 + 97) for i in range(L)]
print('由密文转换为明文：{0}'.format(''.join(N_C_rev)))


