##### Comments on the file for future changes###

area=100 # this is the initial area area=1 area=0 import numpy as np import matplotlib.pyplot as plt

b=3.6
h=2.2
r=1

area = 0.5*b*h
area_circle = np.pi*r**2 

print(area) # Print area of the triangle
print(area_circle) # Print area of the circle

x = np.linspace(0, 2 *np.pi,101)
y = np.sin(x)

plt.plot(x,y)

 
# the input values of the file have changed 
