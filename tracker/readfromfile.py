import numpy as np
import matplotlib.pylab as plt
import re

ar = np.zeros((60,94))

with open('asdf') as file:
    line = file.readline()
    while (line):
        l = [float(s) for s in re.findall("\d+\.\d+",line)]
        if l:
            x = round(l[0] * 10)
            y = round(l[1] * -10)

            print(x,y)
            ar[y,x] = 1

        line = file.readline()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(ar, interpolation='nearest', cmap=plt.cm.ocean)
    # plt.colorbar()
    plt.show()
