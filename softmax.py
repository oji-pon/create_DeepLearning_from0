#np.sum(y) = 1になる
#yの値を確率として解釈できる
import numpy as np
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a -c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
