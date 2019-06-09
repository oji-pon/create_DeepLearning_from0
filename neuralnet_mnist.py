
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
from activation_function import sigmoid
from softmax import softmax
import pickle



def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False )
    #x_test = 1, t_test = 2
    return (x_test, t_test)

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network,x):
    w1, w2, w3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()

accuracy_count = 0
for i in range(len(x)):
    y = predict(network, x[i])
    if t[i] == np.argmax(y):
        accuracy_count += 1

print("Accuracy:" + str(float(accuracy_count) / len(x)))
