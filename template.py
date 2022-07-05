


from ctypes import addressof
from select import select

from sys import stdout
from typing import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import json
import requests
import threading
import time
import sched

#shell process to launch leshan client 
p = 'None'
useCase = 'None'

        #make drop menus clickabel
        self.useCase_dropBox.activated.connect(self.selectUseCase)
        
        # link buttons to methods
        self.chooseUseCase_selectButton.clicked.connect(self.selectUseCase)

        #add options to drop menu
        self.useCase_dropBox.addItem("")
        self.useCase_dropBox.addItem("Bike tracking")
        self.useCase_dropBox.addItem("Eclairage public")
        self.useCase_dropBox.addItem("Qualité de l'air")
        self.useCase_dropBox.addItem("Poubelles intelligentes")
        self.useCase_dropBox.addItem("Chaîne de froid")
        self.useCase_dropBox.addItem("Salle hors-sac")

def selectUseCase(self):

        useCaseSelction = self.useCase_dropBox.currentText()


        match useCaseSelction:
            case "Bike tracking":
                self.useCaseDescription_display.setText("This is Bike tracking use case description") 
            case "Eclairage public":
                self.useCaseDescription_display.setText("This is Chaîne de froid use case description")
            case "Qualité de l'air":
                self.useCaseDescription_display.setText("This is Qualité de l'air use case description") 

            case "Poubelles intelligentes":
                self.useCaseDescription_display.setText("This is Poubelles intelligentes use case description") 
            case "Chaîne de froid":
                self.useCaseDescription_display.setText("This is Chaîne de froid use case description") 

            case "Chaîne de froid":
                self.useCaseDescription_display.setText("This is Chaîne de froid use case description")  



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())