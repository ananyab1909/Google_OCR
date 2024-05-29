import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

import imagetotext as imgt
import handwriting as hand
import detectlogo as logo
import detectlabel as label

def choice():
    print("Press 1 to disply handwriting")
    print("Press 2 to display the image from text")
    print("Press 3 to detect a label")
    print("Press 4 to detect logo")
    print("Press 5 to exit")
choice()

while True:
    ch=int(input("Enter your choice:"))
    if ch>=5:
        print("Exiting....")
        break
    elif ch==1:
        print("Detecting handwriting...")
        hand.detect_handwritten_ocr('path-to-image')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif ch==2:
        print("Detecting text...")
        imgt.detect_document('path-to-image')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    elif ch==3:
        print("Detecting label...")
        label.detect_labels('path-to-image')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()
    else:
        print("Detecting logo...")
        logo.detect_logos('path-to-image')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice()