import string
import random
import operator

class gene:

  def __init__(self,num):
    self.chars= ''.join(random.choice(string.ascii_lowercase)for _ in range(num))
    self.fittness=0;

population=20
target="Ahmad"
genes = [gene(5) for _ in range(population)]

def ranking():
  for Gene in genes:
    Gene.fittness=0
    for i in range(5):
      if (Gene.chars[i] == target[i]):
        Gene.fittness= Gene.fittness+1

def survival():
   genes.sort(key=operator.attrgetter('fittness'),reverse=True)
   if (genes[0].chars=="ahmad"):
    exit()

def rePop(genes):
  genes=genes[:4]
  pop=0
  offspring=[]
  for i in range(4):
    temp1=gene(5)
    temp2=gene(5)
    for j in range(4):
      temp1.chars=genes[i].chars[:3]+genes[j].chars[3:]
      temp2.chars=genes[j].chars[:3]+genes[i].chars[3:]
      offspring.append(temp1)
      offspring.append(temp2)
  genes=genes+offspring
  ranking()
  survival()
  print(genes[0].chars)
  print(genes[0].fittness)
  genes=genes[:20]

def mutation():
  temp=""
  for g in genes:
    for i in range(5):
      if(random.randint(1,1000)<=3):
        temp+=random.choice(string.ascii_lowercase)
      else:
        temp+= g.chars[i]
    g.chars= temp

for i in range(100):
  print(i)
  ranking()
  survival()
  rePop(genes)
  mutation()


