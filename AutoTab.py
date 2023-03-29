import pygetwindow as gw
import time

windows = gw.getAllWindows()

sleeptime = int(input("Enter time (in seconds) to switch windows"))
input1 = " "
activewindows=[]
while input1 != "":
    i=1
    for window in windows:
       print(i,"\t",window) 
       i+=1
       
    print("Selected Windows:")
    for window in activewindows:
        print(window.title)
        
    input1 = input("\nEnter number to add to active windows, or enter to continue\n")
    if input1 != "":
        activewindows.append(windows[int(input1)-1])

print("Cycling windows now!")

while True:
    for window in activewindows:
        currentwindow = gw.getWindowsWithTitle(window.title)[0]
        currentwindow.restore()
        time.sleep(sleeptime)
        currentwindow.minimize()