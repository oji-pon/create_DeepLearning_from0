import numpy as np
import matplotlib.pyplot as plt
#ブロードキャストに対応している
#x　←　np.arrayを入れても大丈夫
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#恒等関数
def identify_function(x):
    return x

'''
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1, 1,1)
plt.show()
'''
