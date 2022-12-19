import readtracker

readtracker.openSerial()
asd = readtracker.readSerialP()
print(asd)
readtracker.closeSerial()
