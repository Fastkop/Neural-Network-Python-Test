import numpy
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




