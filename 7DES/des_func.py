import numpy as np


# 左旋移位
def Round(data, i):
	if len(data) == 28:
		data = data.reshape((4, 7))
	row, col = data.shape
	res = np.zeros(data.shape, dtype = 'int32')
	if i == 1:
		res[:, :col - 1] = data[:, 1: col]
		res[:, col - 1] = data[:, 0]
	else:
		res[:, :col - 2] = data[:, 2: col]
		res[:, col - 2 :col] = data[:, :2]
	return res

# 合并
def Merge(x, y):
	row, col = x.shape
	res = np.zeros((row, col*2), dtype = 'int32')
	res[:, : col] = x
	res[:, col: col*2] = y
	return res
	
# 分裂成左右两个数据集
def SplitToTwo(data):
	Len = data.shape[0]
	L = [data[i] for i in range(Len // 2)]
	R = [data[i] for i in range(Len // 2, Len)]
	return np.array(L), np.array(R)

# 扩展置换函数
def Expansion(data):
	'''
	Arguments:
		data: 数据右半部分，32位
	Returns:
		res: 8行6列的数据，为下一轮S盒置换的输入
	'''
	data = data.reshape((8, 4))
	res = np.zeros((8, 6), dtype = 'int32')
	res[0:8, 1:5] = data
	res[0,0] = data[7,3]
	res[7,0] = data[6,3]
	res[7,5] = data[0,0]
	res[0,5] = data[1,0]
	for i in range(1, 7):
		res[i, 0] = data[i-1, 3]
		res[i, 5] = data[i+1, 0]
	
	return np.array(res)

# 数据块的S盒替换函数
def Sbox(data, box):
	'''
	Arguments:
		data: 加密后的密文，8行6列数据
		box: 预先定义的Sbox，形状为8*4*16
	Returns:
		res: 每一行的6位数据，进行对应S盒置换，得到4位数据，总共8组这样的数据，得到8行4列的输出
	'''
	res = np.zeros((8, 4), dtype = 'int32')
	ls = []
	for i in range(8):
		inS = data[i, :]
		
		row = inS[0]*2 + inS[5]
		col = inS[1]*8 + inS[2]*4 + inS[3]*2 + inS[4]
		
		val2 = bin(box[i][row][col])[2:]
		if len(val2) < 4:
			val2 = '0'*(4 - len(val2)) + val2
		ls.append(val2)
	for i in range(8):
		for j in range(4):
			res[i][j] = ls[i][j]
	
	return np.array(res)

# 置换函数
def ReplaceFunc(data, box):
	'''
	Arguments:
		data: 待置换数据
		box: 置换表
	Returns:
		res: 对data中的每一项做置换所得结果
	Notes:
		一维数组运算
	'''
	try:
		r, c = data.shape
		data = data.reshape((r*c,))
	except:
		pass
	res = np.zeros(box.shape, dtype = 'int32')
	for i in range(len(box)):
		res[i] = data[box[i]-1]
	return res

# 异或运算函数
def xor(x, y):
	try:
		assert(x.shape == y.shape)
	except:
		x = x.reshape(y.shape)
	res = np.zeros(x.shape, dtype = 'int32')
	try:
		for i in range(x.shape[0]):
			for j in range(x.shape[1]):
				res[i][j] = x[i][j] ^ y[i][j]
	except:
		for i in range(x.shape[0]):
			res[i] = x[i] ^ y[i]
		
	return res

