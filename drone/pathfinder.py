import numpy as np

ar = np.array([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ])

def path(j,k,tj,tk):
    ar[j,k] = 1
    while True:
        steps0 = tj - j
        if steps0 != 0:
            steps0 = steps0 / abs(steps0)
        # print("j ",j,"steps0 ",steps0,)

        steps1 = tk - k
        if steps1 != 0:
            steps1 = steps1 / abs(steps1)
        # print("k ",k,"steps1 ",steps1,)

        j = int(j + steps0)
        k = int(k + steps1)

        ar[j,k] = 1
        if j == tj  and k == tk:
            break

# conv(j,k,tj,tk)
path(4,1,0,3)

print(ar)
