# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from csv import list_dialects
from ctypes.wintypes import LPWIN32_FIND_DATAA
from gc import callbacks
import threading
from time import sleep
from turtle import showturtle
from PyQt5 import QtCore, QtGui, QtWidgets

import settings
import time
from clientConnex import connectIface_function,p
from simulationEvents import sendEvent, loadEventList
from loadUseCase import loadUseCaseObjects
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
                          
from datetime import datetime  
from TESTLOG import sendPeriod, sendThread
import logging
from lwm2mSniff import lwm2mSniffer


count=0
logging.basicConfig(level=logging.WARNING)
#connexion_status = 'None'logTextToShow#simulationStatus = "OFF"

sentResources=[]
LOGlist = ""
pausedTime ='None'
class stopWatch(QThread):
    
    def __init__(self,Ui_Widget) -> None:
        self.Ui_Widget = Ui_Widget
      
        #self.Ui_Widget.timeSignal.connect(self.startTime)
    def startTime(self):
        startTime = time.time()
        self.timeSignal.emit()

        pass
    def stop(self):
        pass
    def restart(self):
        pass

class Ui_Widget(QtCore.QObject):

    dataSentSignal = pyqtSignal()    
    startSimulationSignal = pyqtSignal()
    stopSimulationSignal = pyqtSignal()

    

        
        
    def setupUi(self, Widget):
        #global lw_sniffer


        Widget.setObjectName("Widget")
        Widget.resize(876, 634)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 862, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(490, 0, 16, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.useCase_dropBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.useCase_dropBox.setGeometry(QtCore.QRect(10, 50, 181, 22))
        self.useCase_dropBox.setObjectName("useCase_dropBox")
        self.chooseUseCase_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.chooseUseCase_label.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.chooseUseCase_label.setFont(font)
        self.chooseUseCase_label.setObjectName("chooseUseCase_label")
        self.useCaseDescription_display = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.useCaseDescription_display.setGeometry(QtCore.QRect(220, 30, 201, 121))
        self.useCaseDescription_display.setObjectName("useCaseDescription_display")
        self.startSimulation_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.startSimulation_button.setGeometry(QtCore.QRect(610, 170, 101, 21))
        self.startSimulation_button.setStyleSheet("background-color :rgb(66, 170, 37);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-color:black;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.startSimulation_button.setObjectName("startSimulation_button")
        self.stopSimulation_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.stopSimulation_Button.setGeometry(QtCore.QRect(610, 210, 101, 21))
        self.stopSimulation_Button.setStyleSheet("background-color :red;\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-color:black;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.stopSimulation_Button.setObjectName("stopSimulation_Button")
        self.sendingDataPeridod_Input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sendingDataPeridod_Input.setGeometry(QtCore.QRect(680, 90, 101, 20))
        self.sendingDataPeridod_Input.setObjectName("sendingDataPeridod_Input")
        self.simulationDuration_Input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.simulationDuration_Input.setGeometry(QtCore.QRect(680, 50, 101, 20))
        self.simulationDuration_Input.setObjectName("simulationDuration_Input")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(30, 160, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.configuration_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.configuration_label.setGeometry(QtCore.QRect(540, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.configuration_label.setFont(font)
        self.configuration_label.setObjectName("configuration_label")
        self.simulationDuration_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.simulationDuration_label.setGeometry(QtCore.QRect(520, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.simulationDuration_label.setFont(font)
        self.simulationDuration_label.setObjectName("simulationDuration_label")
        self.sendingDataPeriod_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sendingDataPeriod_label.setGeometry(QtCore.QRect(520, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.sendingDataPeriod_label.setFont(font)
        self.sendingDataPeriod_label.setObjectName("sendingDataPeriod_label")
        self.dataUsage_display = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.dataUsage_display.setGeometry(QtCore.QRect(290, 320, 201, 41))
        self.dataUsage_display.setObjectName("dataUsage_display")
        self.dataUsage_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dataUsage_label.setGeometry(QtCore.QRect(290, 280, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.dataUsage_label.setFont(font)
        self.dataUsage_label.setObjectName("dataUsage_label")
        self.info_display = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.info_display.setGeometry(QtCore.QRect(20, 320, 251, 192))
        self.info_display.setObjectName("info_display")
        self.info_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.info_label.setGeometry(QtCore.QRect(20, 280, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.event_dropBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.event_dropBox.setGeometry(QtCore.QRect(510, 300, 181, 22))
        self.event_dropBox.setObjectName("event_dropBox")
        self.event_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.event_Label.setGeometry(QtCore.QRect(510, 270, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.event_Label.setFont(font)
        self.event_Label.setObjectName("event_Label")
        self.sendEvent_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sendEvent_Button.setGeometry(QtCore.QRect(700, 300, 91, 21))
        self.sendEvent_Button.setStyleSheet("background-color :rgb(255, 170, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-color:black;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.sendEvent_Button.setObjectName("sendEvent_Button")
        self.eventDescription_display = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.eventDescription_display.setGeometry(QtCore.QRect(510, 410, 291, 101))
        self.eventDescription_display.setObjectName("eventDescription_display")
        self.dataDescription_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dataDescription_label.setGeometry(QtCore.QRect(510, 380, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.dataDescription_label.setFont(font)
        self.dataDescription_label.setObjectName("dataDescription_label")
        self.useCase_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.useCase_label.setGeometry(QtCore.QRect(220, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.useCase_label.setFont(font)
        self.useCase_label.setObjectName("useCase_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)



        #make drop menus clickabel
        self.useCase_dropBox.activated.connect(self.selectUseCase)
        self.useCase_dropBox.activated.connect(self.setAvailableEvents)
        self.event_dropBox.activated.connect(self.selectEvent)
        
        # link buttons to methods
        self.startSimulation_button.clicked.connect(self.startSimulation_function)
        #self.startSimulation_button.clicked.connect(self.startLOG)   
        self.stopSimulation_Button.clicked.connect(self.stopSimulation_function)
        self.sendEvent_Button.clicked.connect(self.sendEvent_function)

        #add options to drop menu
        self.useCase_dropBox.addItem("")
        self.useCase_dropBox.addItem("Bike tracking")
        self.useCase_dropBox.addItem("Eclairage public")
        self.useCase_dropBox.addItem("Qualité de l'air")
        self.useCase_dropBox.addItem("Poubelles intelligentes")
        self.useCase_dropBox.addItem("Chaîne de froid")
        self.useCase_dropBox.addItem("Salle hors-sac")

        #for tests
        self.sendingDataPeridod_Input.setText("3")

        #connect signals
        self.dataSentSignal.connect(self.showLog)
        self.dataSentSignal.connect(self.measureData)
        self.startSimulationSignal.connect(self.startWatch) 
        self.stopSimulationSignal.connect(self.stopWatch)
        #self.lw_sniffer.newPacketSignal.connect(self.measureData)

        #add logger box

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.chooseUseCase_label.setText(_translate("Widget", "Choose a use case"))
        self.startSimulation_button.setText(_translate("Widget", "Start simulation"))
        self.stopSimulation_Button.setText(_translate("Widget", "Stop simulation"))
        self.configuration_label.setText(_translate("Widget", "Configuration"))
        self.simulationDuration_label.setText(_translate("Widget", "SImulation duration (s)"))
        self.sendingDataPeriod_label.setText(_translate("Widget", "Sending data period (s)"))
        self.dataUsage_label.setText(_translate("Widget", "Data usage"))
        self.info_label.setText(_translate("Widget", "Info"))
        self.event_Label.setText(_translate("Widget", "Events"))
        self.sendEvent_Button.setText(_translate("Widget", "Send event"))
        self.dataDescription_label.setText(_translate("Widget", "Event description"))
        self.useCase_label.setText(_translate("Widget", "Description"))

    
        

    def sendResource_function(self,resourceList):
        from clientConnex import p
        global t6
        #resourceList=[3411,3336,3346,6]
        # if(simulationStatus == "OFF"):
        #     return 0
            
        
        for presentResource in range(len(resourceList)):
                strSend = "send -c=110 " + str(resourceList[presentResource])+'\n' #strSend = "send " + resourceList[presentResource]+'\n' #"create 3424"
                p.stdin.write(bytes(strSend,encoding='utf8'))
                p.stdin.flush()
        #t6.join()        
    
    def peridoicMode_fucntion(self,sendingPeriod,simulationDuration): #,sendingDataPeridod_Input,resourceList
        global t6
        
        def periodicMode_thread():
            #global count
            
            global sentResources
            while settings.simulationStatus == "ON" and ((time.time() - simulationStartTime) <= simulationDuration):
                #count = count +1
                
                global sentResources
                global LOGlist
                listToSend = loadUseCaseObjects(self.useCase_dropBox.currentText())
                sentResources = listToSend
                LOGlist = LOGlist + str(datetime.now())+ " " +str(sentResources) +'\n' + str(time.time() - simulationStartTime)+'\n'
                #LOGlist.append()
                self.dataSentSignal.emit()
                sendThread.run(self,listToSend)
                
                sleep(sendingPeriod)
                
                
        t6 = threading.Thread(target=periodicMode_thread)
        t6.start()
        
        
                # self.info_display.setText("hello")
                # self.info_display.clear()
                # threading.Timer(4,self.peridoicMode_fucntion).start()
                # self.sendResource_function([3333,3336,3411,10282])
        
        
    def startSimulation_function(self):
        #self.showLog()
        #threading.Thread(target=self.snifflwm2m).start()
        
        
        

        self.startSimulationSignal.emit()
        
        global simulationDuration
        global simulationStartTime
        settings.simulationStatus = "ON"
        if simulationStartTime == 'None':
                simulationStartTime = time.time()
        else:
                simulationStartTime = pausedTime

        simulationDuration = int(self.simulationDuration_Input.text()) #in seconds
        sendingPeriod = int(self.sendingDataPeridod_Input.text())
        resourceList =loadUseCaseObjects(useCaseSelction)
 
        sleep(2)
        listToSend = loadUseCaseObjects(useCaseSelction)
        self.peridoicMode_fucntion(sendingPeriod,simulationDuration)
        
        

    def startPeridicMode(self):
        
        t9= threading.Thread(target=startPeriodicMode_thread)
        t9.start()
#     def startLOG(self):
#         def showLog_thread():
                
#                         self.info_display.setText("Hello")
#                         sleep(2)
#         tLOG=threading.Thread(target =showLog_thread)
#         tLOG.start()

    def stopSimulation_function(self):
        #global simulationStatus
        self.stopSimulationSignal.emit()
        settings.simulationStatus = "OFF"

        


    def selectUseCase(self):
        global lw_sniffer
        lw_sniffer = self.createSniffer()
        global useCaseSelction
        useCaseSelction = self.useCase_dropBox.currentText()
        

        match useCaseSelction:
            case "Bike tracking":
                self.useCaseDescription_display.setText("This is Bike tracking use case description")
                loadUseCaseObjects("Bike tracking")
            case "Eclairage public":
                self.useCaseDescription_display.setText("This is Chaîne de froid use case description")
                loadUseCaseObjects("Eclairage public")
            case "Qualité de l'air":
                self.useCaseDescription_display.setText("This is Qualité de l'air use case description") 
                loadUseCaseObjects("Qualité de l'air")
            case "Poubelles intelligentes":
                self.useCaseDescription_display.setText("This is Poubelles intelligentes use case description") 
                loadUseCaseObjects("Poubelles intelligentes")
            case "Chaîne de froid":
                self.useCaseDescription_display.setText("This is Chaîne de froid use case description") 
                loadUseCaseObjects("Chaîne de froid")        
            case "Salle hors-sac":
                self.useCaseDescription_display.setText("This is salle hors-sac use case description")    
                loadUseCaseObjects("Salle hors-sac")         


    def setAvailableEvents(self):
        global useCaseSelction
        eventSelection = self.event_dropBox.currentText()
        
        match useCaseSelction:
                case "":
                        self.event_dropBox.clear()
                        self.eventDescription_display.clear()
                        
                case "Bike tracking":
                        self.event_dropBox.clear()
                        self.event_dropBox.addItems(["Vélo sorti de la zone autorisée", "Défaillance électrique",""])
                        
                case "Eclairage public":
                        self.event_dropBox.clear()
                        self.event_dropBox.addItems(["Détection de passants", "Défaillance capteurs", "Réception commande-DownLink",""])
                case "Qualité de l'air":
                         self.event_dropBox.clear()
                         self.event_dropBox.addItems(["Dépassement seuil CO2", "Défaillance capteurs",""])
                case "Poubelles intelligentes":
                        self.event_dropBox.clear()
                        self.event_dropBox.addItems(["Niveau de remplissage atteint", "Défaillance capteurs",""])
                        
                case "Chaîne de froid":
                        self.event_dropBox.clear()
                        self.event_dropBox.addItems(["Dépassement seuil température", "Baisse niveau carburant","défaillance capteurs",""])
                case "Salle hors-sac":
                        self.event_dropBox.clear()
                        self.event_dropBox.addItems(["Pic de consommation énergétique","défaillance capteurs",""])

                

        self.event_dropBox.setCurrentText("")
        
    def selectEvent(self): 
        global eventSelection
        eventSelection = self.event_dropBox.currentText()
        match eventSelection:
                case "":
                         self.eventDescription_display.clear()
                #event Bike tracking
                case "Vélo sorti de la zone autorisée":
                        self.eventDescription_display.setText("Vélo sorti de la zone autorisée description")
                case "Défaillance électrique":
                        self.eventDescription_display.setText("Objets défaillance électrique")
                #events Eclairage public
                case "Détection de passants":
                        self.eventDescription_display.setText("objets detéction de passants")
                case "Défaillance capteurs":
                        self.eventDescription_display.setText("objets défaillance capteurs")
                case "éception commande-DownLink":
                        self.eventDescription_display.setText("objet réception commande")
                #events qualité de l'air
                case "Dépassement seuil CO2":
                        self.eventDescription_display.setText("objet dépassment seuil CO2")
                case "Défaillance capteurs":
                        self.eventDescription_display.setText("objet défaillance capteurs")
                #event poubelles intelligents
                case "Niveau de remplissage atteint":
                        self.eventDescription_display.setText("objets niveau de remlissage")
                case "Défaillance capteurs":
                        self.eventDescription_display.setText("objets défaillance capteurs")
                #event chaine de froid
                case "Dépassement seuil température":
                        self.eventDescription_display.setText("objets seuil de temprérature")
                case "Baisse niveau carburant":
                        self.eventDescription_display.setText("objets niveau de carburant")
                case "défaillance capteurs":
                        self.eventDescription_display.setText("objets défaillance capteur")
                #event salle hors sac
                case "Pic de consommation énergétique":
                        self.eventDescription_display.setText("objet consommation énergétique")
                case "défaillance capteurs":
                        self.eventDescription_display.setText("objets défaillance capteurs")
    
    def sendEvent_function(self):
        global p
        global LOGlist
        if settings.simulationStatus == "ON" and ((time.time() - simulationStartTime) <= simulationDuration): 
                eventSelection = self.event_dropBox.currentText()
        
                eventObjectsToSend = loadEventList(eventSelection)
                sendEvent(eventObjectsToSend)
                LOGlist =  str(datetime.now())+ " " +str(eventObjectsToSend) +'\n' +LOGlist 
                self.dataSentSignal.emit()
    def createSniffer(self):
        global lw_sniffer
        def create_createSniffer_thread():
                lw_sniffer = lwm2mSniffer()
                return lw_sniffer
        snifferthread = threading.Thread(target=create_createSniffer_thread)
        snifferthread.start()
    def snifflwm2m(self):
        global lw_sniffer
        pass
                
    def measureData(self):
        from lwm2mSniff import packetLen_global
        
        #while settings.simulationStatus == "ON" and ((time.time() - simulationStartTime) <= simulationDuration):
        self.dataUsage_display.setText(packetLen_global)
        
        

#     def selectEvent(self):loadEventList
    @QtCore.pyqtSlot()
    def showLog(self):
       
       
       global count
       global sentResources
       count = count +1
       global lw_sniffer
       self.info_display.setText(LOGlist)
       
       


    @QtCore.pyqtSlot()
    def stopWatch(self):
        global pausedTime
        pausedTime = time.time()
        return pausedTime

    @QtCore.pyqtSlot()
    def startWatch(self):
        global pausedTime
        global simulationStartTime
        simulationStartTime =  pausedTime
        return simulationStartTime



       
        
       
#case   
#          
if __name__ == "__main__":
    import sys
    #
    settings.init()
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    
    ui.setupUi(Widget)
    threading.Thread(target=connectIface_function).start() 
    
    
    Widget.show()
    #connectIface_function()
    
    sys.exit(app.exec_())