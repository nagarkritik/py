import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100,endpoint=True)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,color="red",linewidth=1.0, linestyle='dotted',label="sine")
plt.plot(x,z,color="green",linewidth=1.0, linestyle="dashed",label="cosine")
plt.xlim(-1,2*np.pi)
plt.ylim(-2,15)
plt.legend(loc='upper left')

m = ["A","B","C","D"]
r1 = [2,5,8,5]
r2 = [3,2,5,7]
y = np.arange(len(m))
plt.xticks(y,m)
plt.bar(y,r1,label='R1')
plt.bar(y,r2,label="R2")
plt.legend(loc="upper right")
plt.show()
