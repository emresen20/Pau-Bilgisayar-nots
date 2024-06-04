import numpy as np
import math
import matplotlib.pyplot as plt

#ti = np.arange(-4,4,0.8)
#yi = [0.6294*math.exp(0.8116*t) + np.random.random()*0.00 for t in ti]
#yi = [0.6294587542*math.exp(0.8116712568*t) + np.random.random()*0.15 for t in ti] normal hali buydu
#yi = np.array([9.92, 6.54, 4.31, 2.84, 1.87, 1.24, 0.81, 0.53, 0.35, 0.23])
#ti = np.array([-4, -3.2, -2.4, -1.6, -0.8, 0.0, 0.8, 1.16, 2.4, 3.2])  
ti = np.array([-4, -3.20, -2.40, -1.60, -0.80, 0.00, 0.80, 1.60, 2.40, 3.20]) #t yi buradan belirle 
yi = np.array([24.75, 13.15, 7.00, 3.72, 1.97, 1.05, 0.56, 0.30, 0.16, 0.08])
#------------------------------------------------------------------------------
plt.scatter(ti, yi, color = 'darkred')
plt.xlabel('ti')
plt.ylabel('yi')
plt.title('Dataset 5', fontstyle = 'italic')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.show()














