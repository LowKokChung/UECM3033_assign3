import numpy as np
from scipy.integrate import odeint

def pend(y, t, b, c):
    [y0, y1] = y
    yp = [b * (y0 - y0 * y1), c * (-y1 + y0 * y1)]
    return yp

if __name__ == "__main__":
    a = 1
    b = 0.2
    y0 = 0.1
    y1 = 1.0
    
    y0p = a * (y0 - y0 * y1)
    y1p = b * (-y1 + y0 * y1)
    
    
    yy0 = [0.1,1.0] #[y0,y1]
    t= np.linspace(0,5, 100)
    sol = odeint(pend,yy0,t, args=(a,b))
    
    import matplotlib.pyplot as plt
    plt.plot(t, sol[:, 0], 'b', label='Prey')
    plt.plot(t, sol[:, 1], 'g', label='Predator')
    plt.legend(loc='best')
    plt.xlabel('Time')
    plt.grid()
    plt.show()
    plt.plot(sol[:,1], sol[:,0])
    plt.ylabel('Predator')
    plt.xlabel('Prey')
    plt.grid()
    plt.show()
   
 #To test the sensitivity  
    yy0 = [0.11,1.0] #[y0,y1]
    t= np.linspace(0,5, 100)
    sol = odeint(pend,yy0,t, args=(a,b))
    
    import matplotlib.pyplot as plt
    plt.plot(t, sol[:, 0], 'b', label='Prey')
    plt.plot(t, sol[:, 1], 'g', label='Predator')
    plt.legend(loc='best')
    plt.xlabel('Time')
    plt.grid()
    plt.show()
    plt.plot(sol[:,1], sol[:,0])
    plt.ylabel('Predator')
    plt.xlabel('Prey')
    plt.grid()
    plt.show()
    
