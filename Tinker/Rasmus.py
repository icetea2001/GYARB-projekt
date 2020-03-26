from tkinter import *

#Klass för rasmus information
class Rasmus:
    def __init__(self, MainWindow, data={}):
        self.MainWindow = MainWindow
        self.items = []

        #extra data som kan behövas, i detta fall KevToCel
        self.data = data

    #skicka data att lägga till på fönstret
    def get_data(self):
        theLabel = Label(self.MainWindow, text="Rasmus personliga information", fg="white", bg="black", font=("Helvetica", 16))
        theLabel.pack()
        theLabel.place(x=620, y=180)
        #lägg till data i lista för att sedan kunna ta bort allt samtidigt
        self.items.append(theLabel)

        theLabel2 = Label(self.MainWindow, text="Trångets södra väg 6", fg="white", bg="black", font=("Helvetica", 16))
        theLabel2.pack()
        theLabel2.place(x=667, y=210)
        self.items.append(theLabel2)

        theLabel3 = Label(self.MainWindow, text="423 42", fg="white", bg="black", font=("Helvetica", 16))
        theLabel3.pack()
        theLabel3.place(x=730, y=240)
        self.items.append(theLabel3)

        tempLabel = Label(self.MainWindow, text=(str(self.data[0]) + " °C"), fg="white", bg="black", font=("Helvetica", 16))
        tempLabel.place(x=1105, y=90)
        self.items.append(tempLabel)

    #ta bort data
    def destroy_data(self):
        for item in self.items:
            item.destroy()