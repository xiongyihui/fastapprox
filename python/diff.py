
import numpy as np
import matplotlib.pyplot as plt

import fastapprox

def fast_log2(x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.fast_log2(v)

    return y

def faster_log2(x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.faster_log2(v)

    return y

def fast_pow2(x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.fast_pow2(v)

    return y

def faster_pow2(x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.faster_pow2(v)

    return y

def fast_pow(c, x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.fast_pow(c, v)

    return y

def faster_pow(c, x):
    y = np.zeros(x.shape, dtype=x.dtype)
    for i, v in enumerate(x):
        y[i] = fastapprox.faster_pow(c, v)

    return y


x = np.linspace(0, 100, 1000)
x = x[1:]
plt.plot(x, np.log2(x))
plt.plot(x, fast_log2(x))
plt.plot(x, faster_log2(x))
plt.show()

plt.plot(x, np.log2(x) - fast_log2(x))
plt.show()
plt.plot(x, np.log2(x) - faster_log2(x))
plt.show()


x = np.linspace(0, 80, 1000)
x = x[1:]
plt.plot(x, np.power(2, x))
plt.plot(x, fast_pow2(x))
plt.plot(x, faster_pow2(x))

x1 = x[:50]
plt.plot(x1, np.power(2, x1) - fast_pow2(x1))
plt.show()
plt.plot(x1, np.power(2, x1) - faster_pow2(x1))
plt.show()
