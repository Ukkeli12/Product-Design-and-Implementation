import serial,keyboard
from time import sleep #Viive jos tarvitaan
ser = serial.Serial('COM14',115200,timeout=1) #Sarjaportin määrittäminen
data = "" #Tiedon tallentaminen
def readline(): #Readline komento
    return ser.readline()
for x in range(2): #Menee terminaali tilaan
    ser.write(b'\r')

ser.write(b'les\r')

while 1:
    data = readline() #Luettu tieto
    print(data)
    if readline() == b'': #Laittaa tulostuksen päälle jos se on jumissa
        ser.write(b'\r')
    if keyboard.is_pressed('q') == True: #Sulkee ohjelman tulostuksen Q painikkeella
        break
    
#ser.write(b'quit\r') #Sulkee ohjelman
ser.close()