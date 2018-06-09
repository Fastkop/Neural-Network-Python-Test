import numpy
<<<<<<< HEAD
import math
import string
import random
import operator

class gene:

  def __init__(self,num):
    self.chars= ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(num))
    self.fittness=0;

population=20
target="Ahmad"
genes = [gene(5) for _ in xrange(population)]

def ranking():
  for Gene in genes:
    for i in range(5):
      if (Gene.chars[i] == target[i]):
        Gene.fittness= Gene.fittness+1

def survival():
   genes.sort(key=operator.attrgetter('fittness'),reverse=True)




=======

def color(m1,m2,w1,w2,b):
  z= m1*w1+m2*w2+b
  return seg(z)

def seg(y):
  return 1/(1+numpy.exp(-y))

w1= numpy.random.randn()
w2= numpy.random.randn()
b= numpy.random.randn()

print(color(2,2.5,w1,w2,b))
>>>>>>> dcd9143372863beb6cc55403fcc8983273c3ae0e
