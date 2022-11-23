import keyboard,json

from time import sleep #Viive jos tarvitaan
from serial import Serial #Sarjaportti kirjasto
from redis import Redis #Redis kirjasto raspberry pi:lle

r = Redis(host='localhost', port=6379, db=0)
ser = Serial('COM14',115200) #Sarjaportin määrittäminen

def lue_komentoja_tulostus(): #Tulostaa sarjaporttiin
    ser.write('\r\r'.encode())
    sleep(1)
    ser.write('lec\r'.encode()) #Komento joka aloittaa komentojen lähettämisen
    sleep(1)
    
    while keyboard.is_pressed('q') != True: #Sulkee ohjelman tulostuksen Q painikkeella
        data = ser.readline() #Tiedon tallentaminen sarjaportista seuraavaan rivin vaihtoon asti
        if(data):
            print(data)
            if (b"DIST" in data and b"AN0" in data and b"AN1" in data and b"AN2" in data):
                data = data.replace("\r\n", "").decode().split(",")
                if("DIST" in data):
                    anchor_Nummber = int(data[data.index("DIST")+1])
                    for i in range(anchor_Nummber):
                        pos_AN = {"id": data[data.index("AN"+str(i))+1], "x": data[data.index("AN"+str(i))+2], "y": data[data.index(
                            "AN"+str(i))+3], "dist": data[data.index("AN"+str(i))+5]}
                        pos_AN = json.dumps(pos_AN)
                        print(pos_AN)
                        r.set('AN'+str(i), pos_AN)
                if("POS" in data):
                    pos = {"x": data[data.index("POS")+1],
                            "y": data[data.index("POS")+2]}
                    pos = json.dumps(pos)
                    print(pos)
                    r.set("pos", pos) 
        
def sulje_komento_sulje_sarjaportti(): #Sulkee sarjaportin
    sleep(1)
    ser.write('quit\r'.encode()) #Sulkee ohjelman
    sleep(1)
    ser.close()

if __name__ == '__main__':
    sleep(1)
    while 1:
        tieto = str(input("Kirjoita komento ja paina enter:\n1 Tulostus päälle\n2 Sulje sarjaportti yhteys\nHUOM! Paina Q halutessasi sulkea sarjaportti tulostuksen\n"))
        if tieto == "1":
            lue_komentoja_tulostus()
        elif tieto == "2":
            sulje_komento_sulje_sarjaportti()
            break
