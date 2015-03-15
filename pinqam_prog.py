#!/usr/bin/python

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, QTimer
from gui_pinqam import Ui_MainWindow as Dlg
import sys
import os
import getpass
import time
import threading
import picamera
from PyQt4.QtGui import QMessageBox


#Variablen
activate = False
led_ = True
wb = 'auto'
directory = '/home/'+getpass.getuser()+'/Desktop/PinQam'
rotation = 0
i = 0
height = 720
width = 250


#Ordner anlegen
if not os.path.exists('/home/'+getpass.getuser()+'/Desktop/PinQam/'):
    command = 'mkdir /home/$USER/Desktop/PinQam/'
    os.system(command)
    
if not os.path.exists(directory+'/Zeitraffer'):
    command = 'mkdir '+directory+'/Zeitraffer'
    os.system(command)

if not os.path.exists(directory+'/Liveview'):
    command = 'mkdir '+directory+'/Liveview'
    os.system(command)

if not os.path.exists(directory+'/Webcam'):
    command = 'mkdir '+directory+'/Webcam'
    os.system(command)

if not os.path.exists(directory+'/Filtereffekte'):
    command = 'mkdir '+directory+'/Filtereffekte'
    os.system(command)

if not os.path.exists(directory+'/Video'):
    command = 'mkdir '+directory+'/Video'
    os.system(command)
    

class MainWindow(QtGui.QDialog, Dlg):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        #Buttons
        self.connect(self.btnAkt, QtCore.SIGNAL("clicked()"), self.aktualisieren)
        self.connect(self.btnAkt_2, QtCore.SIGNAL("clicked()"), self.aktualisieren_timelapse)
        self.connect(self.btnAkt_3, QtCore.SIGNAL("clicked()"), self.aktualisieren_presets)
        self.connect(self.btnAkt_4, QtCore.SIGNAL("clicked()"), self.aktualisieren_filters)
        self.connect(self.btnAkt_5, QtCore.SIGNAL("clicked()"), self.aktualisieren_video)
        self.connect(self.btnAusl, QtCore.SIGNAL("clicked()"), self.takePicture)
        self.connect(self.btnAusl_2, QtCore.SIGNAL("clicked()"), self.takePicture_presets)
        self.connect(self.btnAusl_3, QtCore.SIGNAL("clicked()"), self.takePicture_filter)
        self.connect(self.btnClear, QtCore.SIGNAL("clicked()"), self.clear)
        self.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_2, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_3, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_4, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_5, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnClose_6, QtCore.SIGNAL("clicked()"), self.close)

        self.connect(self.btnStart, QtCore.SIGNAL("clicked()"), self.Start)
        self.connect(self.btnStart_2, QtCore.SIGNAL("clicked()"), self.startVideo)     
        self.connect(self.btnCamOn, QtCore.SIGNAL("clicked()"), self.activateCam)
        self.connect(self.btnCamOff, QtCore.SIGNAL("clicked()"), self.deactivateCam)

        #MenuBar
        self.connect(self.actionSpeicherort, QtCore.SIGNAL("triggered()"), self.saveDirectory)
        self.connect(self.action0, QtCore.SIGNAL("triggered()"), self.rotate_0)
        self.connect(self.action_91, QtCore.SIGNAL("triggered()"), self.rotate_90)
        self.connect(self.action_180, QtCore.SIGNAL("triggered()"), self.rotate_180)
        self.connect(self.action_270, QtCore.SIGNAL("triggered()"), self.rotate_270)
        self.connect(self.actionAktiviert, QtCore.SIGNAL("triggered()"), self.ledActivate)
        self.connect(self.actionDeaktiviert, QtCore.SIGNAL("triggered()"), self.ledDeactivate)
        
        self.connect(self.actionOff, QtCore.SIGNAL("triggered()"), self.setWB_off)
        self.connect(self.actionAuto, QtCore.SIGNAL("triggered()"), self.setWB_auto)
        self.connect(self.actionSunlight, QtCore.SIGNAL("triggered()"), self.setWB_sunlight)
        self.connect(self.actionCloudy, QtCore.SIGNAL("triggered()"), self.setWB_cloudy)
        self.connect(self.actionShade, QtCore.SIGNAL("triggered()"), self.setWB_shade)
        self.connect(self.actionTungsten, QtCore.SIGNAL("triggered()"), self.setWB_tungsten)
        self.connect(self.actionIncandescent, QtCore.SIGNAL("triggered()"), self.setWB_incandescent)
        self.connect(self.actionFlash, QtCore.SIGNAL("triggered()"), self.setWB_flash)
  

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

        #ComboBox Filter fuellen
        filters = ['none', 'negative', 'solarise', 'whiteboard', 'blackboard', 'sketch', 'denoise', 'emboss',
                  'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolour', 'film', 'blur', 'saturation',
                  'colourswap', 'washedout', 'posterise', 'colourpoint', 'colourbalance', 'cartoon']

        self.boxEffects.addItems(filters)

        
#Settings
    
    #LED-activate
    def ledActivate(self):
        global led_
        led_ = True

        return led_


    #LED-activate
    def ledDeactivate(self):
        global led_
        led_ = False

        return led_
        
    #Rotation
    def rotate_0(self):
        global rotation

        rotation = 0
        return rotation

    def rotate_90(self):
        global rotation

        rotation = 90
        return rotation

    def rotate_180(self):
        global rotation

        rotation = 180
        return rotation

    def rotate_270(self):
        global rotation

        rotation = 270
        return rotation
    
    #Weissabgleich
    def setWB_off(self):
        global wb
        wb = 'off'

    def setWB_auto(self):
        global wb
        wb = 'auto'

    def setWB_sunlight(self):
        global wb
        wb = 'sunlight'

    def setWB_cloudy(self):
        global wb
        wb = 'cloudy'

    def setWB_shade(self):
        global wb
        wb = 'shade'

    def setWB_tungsten(self):
        global wb
        wb = 'tungsten'

    def setWB_incandescent(self):
        global wb
        wb = 'incandescent'

    def setWB_flash(self):
        global wb
        wb = 'flash'

        
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


        with picamera.PiCamera() as camera:
            camera.sharpness = (sharpness)
            camera.contast = (contrast)
            camera.brightness = (brightness)
            camera.saturation = (saturation)
            camera.iso = (iso)
            camera.rotation = (rotation)
            camera.resolution = (256, 192)
            #camera.led = (led_)

            camera.capture(directory+'/Liveview/liveview.jpg')
        
        #Foto im Liveview anzeigen
        self.labLive.setPixmap(QtGui.QPixmap(directory+'/Liveview/liveview.jpg'))



    def aktualisieren_timelapse(self):
        with picamera.PiCamera() as camera:
            camera.rotation = (rotation)
            camera.resolution = (256, 192)
            #camera.led = (led_)

            camera.capture(directory+'/Liveview/liveview_timelapse.jpg')

        #Foto im Liveview anzeigen            
        self.labLive_2.setPixmap(QtGui.QPixmap(directory+'/Liveview/liveview_timelapse.jpg'))

    def aktualisieren_presets(self):
        preset = self.getPreset()
        preset = str(preset)
        command = 'raspistill -t 300 -w 256 -h 192 -ex '+preset+' -rot %i -o '+directory+'/Liveview/liveview_presets.jpg -n'
        os.system(command % (rotation))

        #Foto im Liveview anzeigen            
        self.labLive_3.setPixmap(QtGui.QPixmap(directory+'/Liveview/liveview_presets.jpg'))

    def aktualisieren_filters(self):
        effect = self.boxEffects.currentText()
        effect = str(effect)

        with picamera.PiCamera() as camera:
            camera.rotation = (rotation)
            camera.resolution = (256, 192)
            camera.image_effect = (effect)
            camera.awb_mode = (wb)
            #camera.led = (led_)

            camera.capture(directory+'/Liveview/liveview_effect.jpg')

        #Foto im Liveview anzeigen            
        self.labLive_5.setPixmap(QtGui.QPixmap(directory+'/Liveview/liveview_effect.jpg'))

    def aktualisieren_video(self):
        with picamera.PiCamera() as camera:
            camera.rotation = (rotation)
            camera.resolution = (256, 192)
            camera.awb_mode = (wb)
            #camera.led = (led_)

            camera.capture(directory+'/Liveview/liveview_video.jpg')

        #Foto im Liveview anzeigen            
        self.labLive_6.setPixmap(QtGui.QPixmap(directory+'/Liveview/liveview_video.jpg'))
    
        

    def takePicture(self):
        #Werte einlesen
        sharpness   = self.boxSharpness.value()
        contrast    = self.boxContrast.value()
        brightness  = self.boxBrightness.value()
        saturation  = self.boxSaturation.value()
        iso         = self.boxIso.value()

        date = time.asctime()
        date = date.replace(' ', '_')
        date = date.replace(':', '_')


        with picamera.PiCamera() as camera:
            camera.sharpness = (sharpness)
            camera.contast = (contrast)
            camera.brightness = (brightness)
            camera.saturation = (saturation)
            camera.iso = (iso)
            camera.rotation = (rotation)
            camera.awb_mode = (wb)
            #camera.led = (led_)

            file = directory+'/Foto_%s.jpg'
            camera.capture(file % (date))


    def takePicture_presets(self):
        preset = self.getPreset()
        preset = str(preset)           
        command = 'raspistill -t 300 -ex '+preset+' -rot %i -o '+directory+'/Foto_preset.jpg -n'
        os.system(command % (rotation))


    def takePicture_filter(self):
        date = time.asctime()
        date = date.replace(' ', '_')
        date = date.replace(':', '_')

        effect = self.boxEffects.currentText()
        effect = str(effect)
        
        with picamera.PiCamera() as camera:
            camera.image_effect = (effect)
            camera.rotation = (rotation)
            camera.awb_mode = (wb)

            file = directory+'/Filtereffekte/Foto_filter_%s.jpg'
            camera.capture(file % (date))


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
        i=1

        #Time Lapse - Schleife
        while bilderzahl>0:
            bilderzahl -=1
            command = 'raspistill -t 300 -rot %i -o '+directory+'/Zeitraffer/Zeitraffer%i.jpg.jpg -n &'
            os.system(command % (rotation, i))
            self.progressBar.setValue(i)
            time.sleep(zeiteinheit/1000)
            i+=1

    def startVideo(self):
        width  = int(self.lineWidth.text())
        height = int(self.lineHeight.text())
        duration = int(self.lineDuration.text())

        #Input-Ueberpruefung
        if (width < 64) or (width > 1920):
            self.msgBox1 = QMessageBox()
            self.msgBox1.setText("Wert fuer Breite ueberpruefen")            
            self.msgBox1.exec_()

        elif (height < 64) or (height >1080):
            self.msgBox2 = QMessageBox()
            self.msgBox2.setText("Wert fuer Hoehe ueberpruefen")            
            self.msgBox2.exec_() 
         
         #Videostabilisator
         if self.radio_stabOn.isChecked()
            video_stabilization = True
            
        elif self.radio_stabOff.isChecked()
            video_stabilization = False
         
        date = time.asctime()
        date = date.replace(' ', '_')
        date = date.replace(':', '_')

        if self.radioMjpeg.isChecked():
            format_ = 'mjpeg'
            
        elif self.radioH264.isChecked():
            format_ = 'h264'
  
        
        with picamera.PiCamera() as camera:
            camera.resolution = (width, height)
            camera.start_recording(directory+'/Video/video_'+date+'.'+format_, format = None)
            camera.wait_recording(duration)
            camera.stop_recording()

        
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
            with picamera.PiCamera() as camera:
                camera.rotation = (rotation)
                camera.resolution = (256, 192)
                camera.awb_mode = (wb)
                #camera.led = (led_)

                camera.capture(directory+'/Webcam/liveview_webcam.jpg')

            #Zeitstempel
            self.labTime.setText(time.asctime())

            #Foto anzeigen
            self.labLive_4.setPixmap(QtGui.QPixmap(directory+'/Webcam/liveview_webcam.jpg'))


    def saveDirectory(self):
        global directory
        
        temp = QtGui.QFileDialog.getExistingDirectory(self, "Speicherort waehlen", "", )
        
        if not temp == "":
            directory = temp
            directory = str(directory)

        #Ordner anlegen
        if not os.path.exists(directory+'/Zeitraffer'):
            command = 'mkdir '+directory+'/Zeitraffer'
            os.system(command)

        if not os.path.exists(directory+'/Liveview'):
            command = 'mkdir '+directory+'/Liveview'
            os.system(command)

        if not os.path.exists(directory+'/Webcam'):
            command = 'mkdir '+directory+'/Webcam'
            os.system(command)

        if not os.path.exists(directory+'/Filtereffekte'):
            command = 'mkdir '+directory+'/Filtereffekte'
            os.system(command)

        if not os.path.exists(directory+'/Video'):
            command = 'mkdir '+directory+'/Video'
            os.system(command)

        return directory

        
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
