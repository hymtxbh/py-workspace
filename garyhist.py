from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
src=Image.open('0.bmp')
r,g,b=src.split()

plt.figure("8")
ar=np.array(r).flatten()
plt.hist(ar, bins=256, density=1,facecolor='r',edgecolor='r')
ag=np.array(g).flatten()
plt.hist(ag, bins=256, density=1, facecolor='g',edgecolor='g')
ab=np.array(b).flatten()
plt.hist(ab, bins=256, density=1, facecolor='b',edgecolor='b')
plt.show()