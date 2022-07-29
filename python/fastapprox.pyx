
cdef extern from "fastlog.h":

    float fastlog2(float x)
    float fastlog(float x)
    float fasterlog2(float x)
    float fasterlog(float x)

def fast_log2(float x):
    return fastlog2(x)

def fast_log(float x):
    return fastlog(x)

def faster_log2(float x):
    return fasterlog2(x)

def faster_log(float x):
    return fasterlog(x)

cdef extern from "fastpow.h":

    float fastpow2(float x)
    float fastexp(float x)
    float fasterpow2(float x)
    float fasterexp(float x)
    float fastpow(float x, float p)
    float fasterpow(float x, float p)

def fast_pow2(float x):
    return fastpow2(x)

def fast_exp(float x):
    return fastexp(x)

def faster_pow2(float x):
    return fasterpow2(x)

def faster_exp(float x):
    return fasterexp(x)

def fast_pow(float x, float p):
    return fastpow(x, p)

def faster_pow(float x, float p):
    return fasterpow(x, p)