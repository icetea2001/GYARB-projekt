from tkinter import *

MainWindow = Tk()
Face = ""

width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d+0+0" % (width_value, height_value))

def RunFaceRecognition():
    return "Rasmus"

Face = RunFaceRecognition()

if Face == "Rasmus":
    print("Rasmus personliga infromation")
else:
    print("Isac personliga infromation")

MainWindow.mainloop()