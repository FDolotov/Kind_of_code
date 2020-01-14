import random
import math

def Log(p):
    V = random.uniform(0,1)
    if V >= p:
        return(1.0)
    U = random.uniform(0,1)
    y = 1.0 - math.exp(U / (1.0 / math.log(1.0 - p)))
    if V > y:
        return(1.0)
    if V <= y * y:
        return(round(1.0 + math.log(V) / math.log(y)))
    return(2.0)

smp = [5,10,100,1000,100000]   #Код для 2 дз
for i in range(len(smp)):
    for j in range(1,6):
        file = open('Log{}.txt'.format('{}_{}'.format(smp[i], j)), 'w')
        for k in range(smp[i]):
             file.write(str(Log(0.2))+' ')
