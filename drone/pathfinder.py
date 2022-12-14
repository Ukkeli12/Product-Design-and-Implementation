from djitellopy import Tello
import numpy as np
import matplotlib.pylab as plt
import time

np.set_printoptions(threshold=np.inf)
H = -99
e = 7
s = 6
p = -1

ar1 = np.array([
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,0,0,0,0,0,0,0,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,0,0,0,0,0,0,0,p,p,p,H,H],
    [H,H,p,p,p,e,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,s,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,H,H,H,H,H,H,H,H,H,H,H,H,H,H,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,p,p,p,0,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,0,p,p,p,H,H],
    [H,H,p,p,p,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,H,H],
    [H,H,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H],
    [H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H,H],
    ])
ar = np.copy(ar1)
ar2 = np.copy(ar)

def getVectors(sj,sk,ej,ek,coordinates):
    coordinates.append((100,100))
    x1,y1= 0,0
    x2,y2= sj,sk
    jvec = 0
    kvec = 0
    vectorList = []
    xflag, yflag = 0,0
    counter = 0
    for i in coordinates:
        counter += 1
        x1,y1 = i[0],i[1]
        if x1 == x2 and yflag == 0:
            jvec += 1
            xflag = 1
            direction = y1-y2
            print(y1-y2," jvec: ",jvec," x,y ",x1,y1," ",i)
            oldi = i
        elif y1 == y2 and xflag == 0:
            kvec += 1
            yflag = 1
            direction = x2-x1
            print(x2-x1," kvec: ",kvec," x,y ", x1,y1," ",i)
            oldi = i
        else:
            if (xflag or yflag == 1):
                print("===================")
                # jvec = jvec * (y1-y2)
                # kvec = kvec * (x2-x1)
                vectorList.append((jvec,kvec,direction,oldi))
                jvec,kvec = 0,0
                xflag = 0
                yflag = 0
        x2,y2 = i[0],i[1]

    return(vectorList)

def checkAdjacentCells(tempAdjacentCells,counter):
    adjacentCells = []
    for a in tempAdjacentCells:
        j = a[0] - 1
        k = a[1] - 1
        for i in range(3):
            for n in range(3):
                if (i == 0 and n == 0) or (i == 2 and n == 0):
                    continue
                if (i == 0 and n == 2) or (i == 2 and n == 2):
                    continue
                # print(i,n)
                if ar[j+i,k+n] == 0:
                    if (j+i,k+n,counter) not in tempAdjacentCells or adjacentCells:
                        ar[j+i,k+n] = str(counter)
                        adjacentCells.append((j+i,k+n,counter))

    return adjacentCells + tempAdjacentCells

def getStartAndEnd():
    asdf = ar.shape
    print(asdf)
    x,y = asdf[0],asdf[1]
    sj,sk,ej,ek = 0,0,0,0
    for i in range(x):
        for n in range(y):
            if ar[i,n] == s:
                sj,sk = i,n
                ar[i,n] = 0
            if ar[i,n] == e:
                ej,ek = i,n
                ar[i,n] = 0
    return sj,sk,ej,ek

def walker(j,k,counter,lista):
    walkable = []
    walkable.append((j,k))
    sj = j - 1
    sk = k - 1
    while(True):
        flag = 0
        for i in range(3):
            for n in range(3):
                if ar[sj+i,sk+n] == counter - 1:
                    if ar2[sj+i,sk+n] == 7:
                        ar2[sj+i,sk+n] = 100
                        sj,sk = sj+i,sk+n
                        walkable.append((sj,sk))
                        return walkable
                    counter -= 1
                    sj,sk = sj+i,sk+n
                    walkable.append((sj,sk))
                    ar2[sj,sk] = 100
                    flag = 1
                if flag == 1:
                    sj -= 1
                    sk -= 1
                    break
            if flag == 1:
                break

def teppoFlyBack(coordinates):
    reversedCoords = []
    cc = coordinates.copy()
    coordinates.reverse()
    for i in range(len(coordinates)):
        print(i)
        reversedCoords.append([
            coordinates[i][0],
            coordinates[i][1],
            coordinates[i][2]*-1,
            cc[i][3]
            ])

    print(reversedCoords)
    time.sleep(10)
    teppo(reversedCoords)

def teppo(coordinates):

    tello = Tello()

    tello.connect()
    tello.takeoff()

    tello.set_speed(50)
    for i in coordinates:
        if i[0] != 0:
            vec = i[0]*10
            if i[2] == 1:
                print("move_right   ",vec)
                tello.move_right(vec)
            if i[2] == -1:
                print("move_left    ",vec*-1)
                tello.move_left(vec)
        else:
            vec = i[1]*10
            if i[2] == 1:
                print("move_forward ",vec)
                tello.move_forward(vec)
            if i[2] == -1:
                print("move_back    ",vec*-1)
                tello.move_back(vec)
    print("===================")

    tello.land()

def dain(x,y):
    global ar
    global ar2
    # print(ar)
    # print()
    acCounter = 1;
    sj,sk,ej,ek = getStartAndEnd()
    print("afterGetStartAndEnd()")
    ar2[sj,sk] = 100
    if x and y != 0:
        ar2[ej,ek] = 0
        ej,ek = x,y
        ar2[x,y] = 7
    # print(sj,sk)
    # print(ej,ek)
    adjacentCells = [(ej,ek,acCounter)]
    # print("afterAdjacentCells()")
    # print(ej,ek)
    flag = 0
    while(True):
        for i in adjacentCells:
            adjacentCells = checkAdjacentCells(adjacentCells,acCounter)
            for n in adjacentCells:
                if n == (sj,sk,acCounter):
                    ar[ej,ek] = 0
                    flag = 1
                    break
            if flag == 1:
                break
            acCounter += 1
        if flag == 1:
            break
    # print("beforeWalker")

    coordinates = walker(sj,sk,acCounter,adjacentCells)
    coords = getVectors(sj,sk,ej,ek,coordinates)

    print()
    print(coords)
    
    teppo(coords)

    teppoFlyBack(coords)#,sj,sk,ej,ek)


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(ar2, interpolation='nearest', cmap=plt.cm.ocean)
    plt.axis('off')
    # plt.colorbar()
    # plt.savefig('asdf.png',bbox_inches='tight')
    plt.show()

    ar = np.copy(ar1)
    ar2 = np.copy(ar)

# def main():
    # # dain(0,0)
    # dain(20,58)

# if __name__ == main():
    # main()
