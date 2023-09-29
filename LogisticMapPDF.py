import random
import matplotlib.pyplot as plt
import numpy as np

# Logistic map formula
r = 3.7
N = lambda x: r*x*(1-x)
# The max amount of times the map is applied to the initial values
max_t = 50
# The number of initial values
xiCount = 10000
# The initial values
xs = []
# The final values after applying the initial map t times
ys = []

# Starts with an initial value of xi and gets the final value after applying
# the map t times
def getFinal(xi,t):
    xf = xi
    for i in range(t):
        xf = N(xf)
    return xf

# Gradually increases t to show how the distribution changes over time
for t in range(max_t):
    for xi in np.arange(0,1,1/xiCount):
        xf = getFinal(xi,t)
        xs.append(xi)
        ys.append(xf)
        
    plt.clf()
    plt.hist(ys)
    plt.title("Distribution (r="+str(r)+", "+str(xiCount)+" initial values)")
    plt.xlabel("Final value")
    plt.ylabel("Count")
    plt.ylim(0,5500)
    plt.pause(0.05)
    xs = []
    ys = []
    
print("Done")
plt.show()
