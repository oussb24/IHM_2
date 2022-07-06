from concurrent.futures import thread
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
import time
class sendThread(QThread):
    sendOnce_signal = pyqtSignal()
    def run(self,resourceList):
        from clientConnex import p
        
        
        #resourceList=[3333,3336,3411,10282]
        for presentResource in range(len(resourceList)):
                strSend = "send -c=110 " + str(resourceList[presentResource])+'\n' #strSend = "send " + resourceList[presentResource]+'\n' #"create 3424"
                p.stdin.write(bytes(strSend,encoding='utf8'))
        p.stdin.flush()
    
        #self.send_signal.emit()
        	#
    
class sendPeriod(QThread):
    sendPeriod_signal = pyqtSignal()
    def run(self):
        
            sendThread.run(self)
            time.sleep(2)


class stopWatch(QThread):
    def __init__(self,Ui_Widget) -> None:
         self.Ui_Widget = Ui_Widget
         self.Ui_Widget.timeSignal
    def start(self):
        startTime = time.time()
        pass
    def stop(self):
        pass
    def restart(self):
        pass