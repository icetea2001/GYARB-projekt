from tkinter import *

#Klass för isacs info
class Isac:
    def __init__(self, MainWindow, data={}):
        self.MainWindow = MainWindow
        self.items = []

    def get_data(self):
        print("Isac personliga information")
        theLabel = Label(self.MainWindow, text="Isac personliga infromation", fg="white", bg="black")
        theLabel.pack()
        self.items.append(theLabel)

    def destroy_data(self):
        for item in self.items:
            item.destroy()