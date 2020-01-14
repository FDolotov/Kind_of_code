import numpy as np
import time

def Geom(p):
    a, b, c = 0, 0, 0
    while a == 0:
        c = np.random.rand()
        if c < p:
            a = 1
        else:
            b = b + 1
    return b  

"""smp = [5,10,100,1000,1000000]   #Код для 2 дз
for i in range(len(smp)):
    current_time = time.time()
    for j in range(1,6):
        file = open('Geom{}.txt'.format('{}_{}'.format(smp[i], j)), 'w')
        for k in range(smp[i]):
             file.write(str(Geom(0.2))+' ')
    print(time.time() - current_time)"""