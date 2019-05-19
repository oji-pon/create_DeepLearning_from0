import numpy as np

def AND(x1, x2):
    w1, w2 ,b = 0.5, 0.5, -0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    w1, w2 ,b = -0.5, -0.5, 0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    w1, w2 ,b = 0.5, 0.5, -0.2
    x = np.array([x1,x2])
    w = np.array([w1,w2])
    tmp = np.sum(x*w) + b
    if tmp > 0:
        return 1
    else:
        return 0

#XORのパーセプトロン
#非線形な領域を２層のパーセプトロンで実現
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

#結果を出力
a00 = AND(0,0)
a01 = AND(0,1)
a10 = AND(1,0)
a11 = AND(1,1)
print(a00, a01, a10, a11)
b00 = OR(0,0)
b01 = OR(0,1)
b10 = OR(1,0)
b11 = OR(1,1)
print(b00,b01,b10,b11)
c00 = NAND(0,0)
c01 = NAND(0,1)
c10 = NAND(1,0)
c11 = NAND(1,1)
print(c00,c01,c10,c11)
d00 = XOR(0,0)
d01 = XOR(0,1)
d10 = XOR(1,0)
d11 = XOR(1,1)
print(d00,d01,d10,d11)
