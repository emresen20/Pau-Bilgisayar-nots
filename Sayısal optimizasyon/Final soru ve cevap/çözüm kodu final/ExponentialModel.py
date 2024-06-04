import numpy as np
import math
from dataset5 import ti,yi
#-------------------------------------------------------------------------------------
def exponentialIO(t,x): # t -> inputlar, x  -> parametreler
    yhat = []  #tüm çıkışları tanımlamak için kullancağız
    for ti in t:
        toplam = x[0]*math.exp(x[1]*ti)
        yhat.append(toplam)
    return yhat
#-------------------------------------------------------------------------------------

def error(xk,ti, yi):
    yhat = exponentialIO(ti, xk)
    return np.array(yi) - np.array(yhat)  #Gerçek çıktı - Üretilen çıktı
#-------------------------------------------------------------------------------------

def findJacobian(traininginput,x):
    numofdata = len(traininginput)
    J = np.matrix(np.zeros((numofdata,2)))
    for i in range(0, numofdata):
        J[i,0] = -math.exp(x[1]*traininginput[i]) # Jacobian 1. sutün
        J[i,1] = -x[0]*traininginput[i]*math.exp(x[1]*traininginput[i]) # Jacobian 2. sutün
    return J

#-------------------------------------------------------------------------------------

trainingindices = np.arange(0, len(ti), 1)
traininginput = np.array(ti)[trainingindices]
trainingoutput = np.array(yi)[trainingindices]

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

MaxIter = 500
epsilon1 = 1e-9
epsilon2 = 1e-9
epsilon3 = 1e-9
mumax = 1e99

#-------------------------------------------------------------------------------------

x1 = [np.random.random()-0.5]
x2 = [np.random.random()-0.5]

xk = np.array([x1[0], x2[0]])
k = 0; C1 = True; C2 = True; C3 = True; C4 = True; fvalidationBest = 1e99

ek = error(xk, traininginput, trainingoutput)
ftraining = sum(ek**2)
FTRA = [ftraining]
ITERATION = [k]
print('k:',k, 'x1:', format(xk[0],'f'), 'x2:', format(xk[1],'f'),'f',format(ftraining,'f'))
mu = 1; muscal = 10; I = np.identity(2)
while C1 & C2 & C3 & C4:
    ek = error(xk, traininginput, trainingoutput)
    Jk = findJacobian(traininginput,xk)
    gk = np.array((2*Jk.transpose().dot(ek)).tolist()[0]) #Gradient
    Hk = 2 * Jk.transpose().dot(Jk) + 1e-8*I #Heissian
    ftraining = sum(ek**2)
    sk = 1
    loop = True
    while loop:
        zk = -np.linalg.inv(Hk+mu*I).dot(gk) # Aday yön
        zk = np.array(zk.tolist()[0])
        ez = error(xk + sk * zk, traininginput, trainingoutput)
        fz = sum(ez**2)
        if fz < ftraining:
            pk = 1*zk
            mu = mu / muscal
            k += 1
            xk = xk + sk * pk
            x1.append(xk[0])
            x2.append(xk[1])
            loop = False
            print('k:', k, 'x1:', format(xk[0], 'f'), 'x2:', format(xk[1], 'f'), 'f', format(xk[1], 'f'))
        else:
            mu = mu * muscal
            if mu > mumax:
                loop = False
                C2 = False
        FTRA.append(ftraining)
        ITERATION.append(k)
        #----------------------------
    C1 = k < MaxIter
    C2 = epsilon1 < abs(ftraining-fz)
    C3 = epsilon2 < np.linalg.norm(sk*pk)
    C4 = epsilon3 < np.linalg.norm(gk)
        #-----------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
T = np.arange(min(ti), max(ti), 0.1)
yhat = exponentialIO(T, xk)
plt.scatter(ti,yi, color = 'darkred', marker = 'x')
plt.plot(T, yhat, color = 'green', linestyle = 'solid', linewidth = 1)
plt.xlabel('ti')
plt.ylabel('yi')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.legend(['ustel model', 'gercek veri'])
plt.show()

#-------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
plt.plot(ITERATION, FTRA, color = 'green', linestyle = 'solid', linewidth = 1)
plt.xlabel('iterasyon')
plt.ylabel('eğitim hatası')
plt.title('performans', fontstyle = 'italic')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.legend(['training'])
plt.show()
#-------------------------------------------------------------------------------------------





