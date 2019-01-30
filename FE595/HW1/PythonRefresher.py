import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi, 201) # get the x- axis horizon
plt.plot(x, np.sin(x), label='sine')  #plot sine
plt.plot(x, np.cos(x), label='cosine') #plot cosine
plt.legend(loc='best') # put the legend in the suitable place
plt.xlabel('Angle ') #set the x label
plt.ylabel('sin(x) and cos(x)') # set the y-label
plt.axis('tight')
plt.title('FE595 first assginment') #set the title
plt.savefig('PythonRefresher.png') #save my image
plt.show()