#Use NumPy and MatPlotLib to graph one period of sine and cosine on the same set of axes

import matplotlib.pyplot as plt
import numpy as np
from pylab import *

# Synopsis
# The np sin & cos functions take an array_like and return an array_like
# Docs : https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin


#Create an array of angle values for 1 time period
x_angles = np.linspace(0, 2*np.pi, 100)

plt.ylim((-1, 1))
# Add the sine and cosine of the values in x_angles array)like
plt.plot(x_angles , np.sin(x_angles ))
plt.plot(x_angles , np.cos(x_angles ))
plt.plot(x_angles , np.tan(x_angles ))

# Add Labels
plt.title('Sine , Cosine  and tangent wave')
plt.xlabel('Radians')
plt.ylabel('Sin & Cos & tan values')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
#plt.axis('tight')

plt.savefig('PythonCollab.png') 
# Show chart
plt.show()