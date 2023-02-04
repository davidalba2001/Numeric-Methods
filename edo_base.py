import numpy as np
import matplotlib.pyplot as plt

#Funcion 
f =  lambda x,y : x+y**1/3

def Numeric_Methods(X0,Y0,h,hx,f,method,range_end):
     xn = np.arange(X0,range_end+hx,hx)
     yn = [Y0]
     for i in range(0,len(xn)-1):
        yn.append(round(method(xn[i],yn[i],h,hx,f),6))
     return xn,yn

# Metodos de Euler

def Method_euler(Xn,Yn,h,hx,f):
    yn1 = Yn + h * f(Xn,Yn)
    return yn1

# Metodos de Euler Mejorado

def Method_eulerMejorado(Xn,Yn,h,hx,f):
      k1 = f(Xn,Yn)
      un1 = Yn + h * k1 
      k2 = f(Xn+hx,un1)
      yn1 = Yn + h * 1/2*(k1 + k2)
      return yn1

# Metodos de Runge Kutta

def Runge_Kutta(Xn,Yn,h,hx,f):

     k1 = f(Xn,Yn)
     k2 = f( Xn +(1/2)*h,Yn+(1/2)*h*k1)
     k3 = f(Xn +(1/2)*h,Yn+(1/2)*h*k2)
     k4 = f(Xn + hx,Yn+ h*k3)
     Yn1 = Yn + h/6 *(k1 + 2*k2 + 2*k3 + k4)
     return Yn1

# Plotear los metodos numericos
ptosEuler1 = Numeric_Methods(0,-1,0.1,0.1,f,Method_euler,2)
ptosEulerM1 = Numeric_Methods(0,-1,0.5,0.1,f,Method_eulerMejorado,2)
ptosRunge1 = Numeric_Methods(0,-1,0.5,0.1,f,Runge_Kutta,2)
plt.plot(ptosEuler1[0],ptosEuler1[1])
plt.plot(ptosEulerM1[0],ptosEulerM1[1])
plt.plot(ptosRunge1[0],ptosRunge1[1])
ptosEuler = Numeric_Methods(0,-1,0.2,0.1,f,Method_euler,2)
ptosEulerM = Numeric_Methods(0,-1,0.2,0.1,f,Method_eulerMejorado,2)
ptosRunge = Numeric_Methods(0,-1,0.2,0.1,f,Runge_Kutta,2)
plt.plot(ptosEuler[0],ptosEuler[1])
plt.plot(ptosEulerM[0],ptosEulerM[1])
plt.plot(ptosRunge[0],ptosRunge[1])
plt.show()