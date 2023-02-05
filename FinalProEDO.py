import numpy as np
import matplotlib.pyplot as plt
import math as mth

def Kn(k1,k2,k3,k4):
    return (k1+2*k2+2*k3+k4)/6

def runge_kuta(x0,t0,tf,fn,h,ro):
    Xn = x0
    tn = t0
    t_values = [tn]
    func_values =[x0]
    
    while(min(tn) <= tf):
        k1 = fn(tn,Xn)
        k2 = fn(tn + 1/2*h,Xn+1/2*h*k1)
        k3 = fn(tn + 1/2*h,Xn+1/2*h*k2)
        k4 = fn(tn +h,Xn+h*k3)
        Xn1 = Xn + h*Kn(k1,k2,k3,k4)
        #Actualiza los valores para la proxima iteracion
        Xn = Xn1
        tn = tn + h
        #Guardo los valores
        t_values.append([round(t,ro) for t in tn])
        func_values.append([round(x,ro) for x in Xn1])
    return t_values,func_values


#Eq.1 
c = 0.00001
m2 = 0.03
p1 = 0.1245
g1 = 2*10**7
#Eq.2
g2 = 10**5
r2 = 0.18
b = 10**-9
a = 1
#Eq.3
m3 = 10
p2 = 5
g3 = 10**3
