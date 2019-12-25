from utils_key import *
from utils_prodtrans import *

# 生成明文
m = np.random.randint(0, 2, 64)

# 初始置换并分裂成左右两部分
m0 = ReplaceFunc(m, DesInitial)
L, R = SplitToTwo(m0)

# 16轮乘积变换
for i in range(16):
	L, R = ProductTrans(L, R, i)

# 合并左右两部分并作逆初始置换
c = Merge(L, R)
c = ReplaceFunc(c, DesInverse)

print('明文(随机生成)：', m)
print('密文：', c)