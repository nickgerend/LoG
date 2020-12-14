# Written by: Nick Gerend, @dataoutsider
# Viz: "LoG", enjoy!

import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Laplacian of Gaussian filter used for edge detection!
def LoG(x, y, sigma):
    zscale = 100000
    ratio = (x**2+y**2)/(2*sigma**2)
    return (-1/(np.pi*sigma**4)*(1-ratio)*np.exp(-ratio))*zscale

N = 49 # odd number for even distribution around 0
n = 500
x = np.linspace(0.0,N,n)
y = np.linspace(0.0,N,n)
Xgrid, Ygrid = np.meshgrid(x, y)

Zgrid = -LoG(Xgrid-N//2, Ygrid-N//2, sigma=6)
Xout = np.reshape(Xgrid, -1)
Yout = np.reshape(Ygrid, -1)
Zout = np.reshape(Zgrid, -1)

gridplot = plt.axes(projection='3d')
gridplot.plot_wireframe(Xgrid, Ygrid, Zgrid, color='g')
plt.show()

import csv
import os
with open(os.path.dirname(__file__) + '/3d_math.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['x', 'y', 'z'])
    for i in range(len(Xout)):
        writer.writerow([Xout[i], Yout[i], Zout[i]])
print('finished')