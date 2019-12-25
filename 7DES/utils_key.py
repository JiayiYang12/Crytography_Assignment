import numpy as np
from des_func import *
from Table import *

# 每一轮都使用不同的子密钥

def GenerateKey(i):
	'''
	Arguments:
		i: 轮数，关系到左旋的位数
	Returns: 
		ki: 第i轮48位密钥
	'''
	k0 = np.random.randint(0, 2, 64) # 随机初始化64位密钥
	k1 = ReplaceFunc(k0, DesTransform) # PC1置换
	L0, R0 = SplitToTwo(k1) # 分裂成两个数据集合
	L1 = Round(L0, i) # 左表左旋
	R1 = Round(L0, i) # 右表左旋
	k2 = Merge(L1, R1) # 合并两张表
	r, c = k2.shape
	k2 = k2.reshape((r * c, 1))
	ki = ReplaceFunc(k2, Despermutated) # PC2置换
	ki = ki.reshape((8, 6))
	return ki
