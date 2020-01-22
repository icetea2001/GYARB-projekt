from tkinter import *

MainWindow = Tk()
Face = ""

width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
MainWindow.wm_attributes('-fullscreen', 'true')
MainWindow.configure(background="black")

def RunFaceRecognition():
    return "Rasmus"

Face = RunFaceRecognition()

if Face == "Rasmus":
    print("Rasmus personliga infromation")
    theLabel = Label(MainWindow, text="Rasmus personliga infromation", fg="white", bg="black")
    theLabel.pack()

    #Lägg in din skit här Isac.

else:
    print("Isac personliga infromation")
    theLabel = Label(MainWindow, text="Isac personliga infromation", fg="white", bg="black")
    theLabel.pack()

    #Lägg in din skit här Isac.

MainWindow.mainloop()