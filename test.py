import numpy

def color(m1,m2,w1,w2,b):
  z= m1*w1+m2*w2+b
  return seg(z)

def seg(y):
  return 1/(1+numpy.exp(-y))

w1= numpy.random.randn()
w2= numpy.random.randn()
b= numpy.random.randn()

print(color(2,2.5,w1,w2,b))
