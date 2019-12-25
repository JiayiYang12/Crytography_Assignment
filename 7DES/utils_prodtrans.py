from utils_key import *

def ProductTrans(L0, R0, i):
	'''
	Arguments:
		L0: 第i-1轮输入数据的左半部分
		R0: 第i-1轮输入数据的右半部分
		i: 轮数
	Returns:
		Li: 第i轮的输入的左半部分
		Ri: 第i轮的输入的右半部分
	'''
	R1 = Expansion(R0) # 选择扩展运算E
	key = GenerateKey(i) # 生成密钥
	R2 = xor(R1, key) # 密钥加密运算
	R3 = Sbox(R2, S_box) # 选择压缩运算S
	R4 = ReplaceFunc(R3, P_box) # 置换运算P
	R5 = xor(R4, L0) # 左右做异或运算
	Ri = R5.reshape((8, 4))
	Li = R0.reshape((8, 4))
	return Li, Ri