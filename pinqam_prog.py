#!/usr/bin/python

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, QTimer
from gui_pinqam import Ui_MainWindow as Dlg
import sys
import os
import getpass
import time

#Ordner anlegen
if not os.path.exists('/home/'+getpass.getuser()+'/Desktop/PinQam/'):
    command = 'mkdir /home/$USER/Desktop/PinQam/'
    os.system(command)

#Zeitraffer - Ordner anlegen
if not os.path.exists('/home/'+getpass.getuser()+'/Desktop/PinQam/Zeitraffer'):
    command = 'mkdir /home/$USER/Desktop/PinQam/Zeitraffer'
    os.system(command)

#Variablen
activate = False


class MainWindow(QtGui.QDialog, Dlg):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        #Buttons
        self.connect(self.btnAkt, QtCore.SIGNAL("clicked()"), self.aktualisieren)
        self.connect(self.btnAkt_2, QtCore.SIGNAL("clicked()"), self.aktualisieren_timelapse)
        self.connect(self.btnAkt_3, QtCore.SIGNAL("clicked()"), self.aktualisieren_presets)
        self.connect(self.btnAusl, QtCore.SIGNAL("clicked()"), self.takePicture)
        self.connect(self.btnAusl_2, QtCore.SIGNAL("clicked()"), self.takePicture_presets)
        self.connect(self.btnClear, QtCore.SIGNAL("clicked()"), self.clear)
        self.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_2, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_3, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_4, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnStart, QtCore.SIGNAL("clicked()"), self.Start)
        self.connect(self.btnCamOn, QtCore.SIGNAL("clicked()"), self.activateCam)
        self.connect(self.btnCamOff, QtCore.SIGNAL("clicked()"), self.deactivateCam)

        #Timer fuer Webcam
        self.timer = QTimer()
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.Webcam)
        self.timer.start(3000)

        #Progressbar auf 0 setzen
        self.progressBar.setValue(0)

        #ComboBox Presets fuellen
        presets = ['antishake', 'automatisch', 'Feuerwerk', 'heller Hintergrund', 'Langzeitbelichtung',
                  'Nachtaufnahme', 'Schnee', 'Sport', 'Strand']        
        self.boxPresets.addItems(presets)
        
    #Motivprogrammauswahl abrufen und uebersetzen
    def getPreset(self):
        preset = self.boxPresets.currentText()

        if preset == 'automatisch':
            preset = 'auto'

        elif preset == 'Feuerwerk':
            preset = 'fireworks'

        elif preset == 'heller Hintergrund':
            preset = 'backlight'

        elif preset == 'Langzeitbelichtung':
            preset = 'verylong'

        elif preset == 'Nachtaufnahme':
            preset = 'night'

        elif preset == 'Schnee':
            preset = 'snow'

        elif preset == 'Sport':
            preset = 'sports'

        elif preset == 'Strand':
            preset = 'beach'

        return preset
            
        
    def aktualisieren(self):            
        #Werte einlesen
        sharpness   = self.boxSharpness.value()
        contrast    = self.boxContrast.value()
        brightness  = self.boxBrightness.value()
        saturation  = self.boxSaturation.value()
        iso         = self.boxIso.value()

        command = 'raspistill -t 300 -sh %i -co %i -br %i -sa %i -ISO %i -w 256 -h 192 -o /home/'+getpass.getuser()+'/Desktop/PinQam/liveview.jpg -n'
        os.system(command % (sharpness, contrast, brightness, saturation, iso))
        
        #Foto im Liveview anzeigen
        self.labLive.setPixmap(QtGui.QPixmap('/home/'+getpass.getuser()+'/Desktop/PinQam/liveview.jpg'))

    def aktualisieren_timelapse(self):
        command = 'raspistill -t 300 -w 256 -h 192 -o /home/'+getpass.getuser()+'/Desktop/PinQam/liveview_timelapse.jpg -n'
        os.system(command)

        #Foto im Liveview anzeigen            
        self.labLive_2.setPixmap(QtGui.QPixmap('/home/'+getpass.getuser()+'/Desktop/PinQam/liveview_timelapse.jpg'))

    def aktualisieren_presets(self):
        preset = self.getPreset()
        preset = str(preset)
        command = 'raspistill -t 300 -w 256 -h 192 -ex '+preset+' -o /home/'+getpass.getuser()+'/Desktop/PinQam/liveview_presets.jpg -n'
        os.system(command)

        #Foto im Liveview anzeigen            
        self.labLive_3.setPixmap(QtGui.QPixmap('/home/'+getpass.getuser()+'/Desktop/PinQam/liveview_presets.jpg'))

    def takePicture(self):
        #Werte einlesen
        sharpness   = self.boxSharpness.value()
        contrast    = self.boxContrast.value()
        brightness  = self.boxBrightness.value()
        saturation  = self.boxSaturation.value()
        iso = self.boxIso.value()

        command = 'raspistill -t 300 -sh %i -co %i -br %i -sa %i -ISO %i -o /home/'+getpass.getuser()+'/Desktop/PinQam/Foto.jpg -n'
        os.system(command % (sharpness, contrast, brightness, saturation, iso))

    def takePicture_presets(self):
        preset = self.getPreset()
        preset = str(preset)           
        os.system('raspistill -t 300 -ex '+preset+' -o /home/'+getpass.getuser()+'/Desktop/PinQam/Foto_preset.jpg -n')
        

    def Start(self):
        #Werte einlesen
        zeitraum    = self.boxZeitraum.value()
        bilderzahl  = self.boxAnzahl.value()
        zeiteinheit = 0

        #Zeitraum und Zeiteinheit bestimmen
        if self.radioSec.isChecked():
            zeitraum *= 1000
            zeiteinheit = zeitraum / bilderzahl
           
        elif self.radioMin.isChecked():
            zeitraum *= 1000 * 60
            zeiteinheit = zeitraum / bilderzahl   

        elif self.radioHour.isChecked():
            zeitraum *= 1000 * 3600
            zeiteinheit = zeitraum / bilderzahl

        #Setup Progressbar
        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(bilderzahl)

        #Zaehlervariable definieren
        i = 1

        #Time Lapse - Schleife
        while bilderzahl > 0:
            bilderzahl -= 1
            command = 'raspistill -t 300 -o /home/'+getpass.getuser()+'/Desktop/PinQam/Zeitraffer/Zeitraffer%i.jpg.jpg -n &'
            os.system(command % (i))
            self.progressBar.setValue(i)
            time.sleep(zeiteinheit / 1000)
            i += 1

    def activateCam(self):
        global activate 
        activate = True
        return activate

    def deactivateCam(self):
        global activate
        activate = False
        return activate
    
    def Webcam(self):
        if activate == True:
            command = 'raspistill -t 300 -w 256 -h 192 -ex auto -o /home/'+getpass.getuser()+'/Desktop/PinQam/liveview_webcam.jpg -n'
            os.system(command)
            
            #Zeitstempel
            self.labTime.setText(time.asctime())

            #Foto anzeigen
            self.labLive_4.setPixmap(QtGui.QPixmap('/home/'+getpass.getuser()+'/Desktop/PinQam/liveview_webcam.jpg'))


        
    def clear(self):
        self.boxSharpness.setValue(0)
        self.boxContrast.setValue(0)
        self.boxBrightness.setValue(0)
        self.boxSaturation.setValue(0)
        self.boxIso.setValue(100)

    def close(self):
        exit()
             
app = QtGui.QApplication(sys.argv)
dialog=MainWindow()
dialog.show()
sys.exit(app.exec_())
