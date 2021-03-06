import numpy as np
from activation_function import sigmoid, identify_function
#ネットワークのの構築（重みパラメータの設定）
def init_network():
    #ネットワーク：辞書型
    network = {}
    network["w1"] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network["w2"] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network["w3"] = np.array([[0.1,0.3],[0.2,0.4]])
    network["b1"] = np.array([0.1,0.2,0.3])
    network["b2"] = np.array([0.1,0.2])
    network["b3"] = np.array([0.1,0.2])

    return network

#処理
def forword(network, x):
    w1, w2, w3 = network["w1"], network["w2"], network["w3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x,w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(a1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = identify_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forword(network, x)
print(y)
