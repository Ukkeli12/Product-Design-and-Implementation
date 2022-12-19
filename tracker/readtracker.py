from serial import Serial #Sarjaportti kirjasto
from time import sleep

def openSerial():
    global ser 
    ser = Serial('/dev/ttyACM3',115200) #Sarjaportin määrittäminen
    ser.write('\r\r'.encode())
    sleep(1)
    ser.write('lec\r'.encode()) #Komento joka aloittaa komentojen lähettämisen
    sleep(1)

def closeSerial():
    sleep(0.2)
    ser.write('quit\r'.encode()) #Sulkee ohjelman
    sleep(0.2)
    ser.close()

def readSerialP():
    try:
        with open('asdf', 'w') as f:
            counter = 0
            m2 = 0
            a2 = 0
            while(True):
                line = ser.readline() 

                m = line.decode("utf-8")
                ma = m.split(',')

                if ma[0] == 'POS':
                    if b'nan' in line:
                        continue
                    a1 = float(ma[3])
                    m1 = float(ma[4])

                    m2 += a1
                    a2 += m1

                    if counter >= 10:
                        m2 = (round(m2,0))/counter
                        a2 = (round(a2,0))/counter
                        asd = str(m2) + " " + str(a2)
                        print(asd)
                        f.write(f"{asd}\n")
                        m2,a2 = 0,0
                        counter = 0
                        return asd
                    counter += 1

    except KeyboardInterrupt:
        print()
        print('Interrupted')
        closeSerial()
