# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_pinqam.ui'
#
# Created: Tue Jun 17 19:50:50 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(571, 394)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 551, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 57, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 57, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 57, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 57, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.boxSharpness = QtGui.QSpinBox(self.groupBox)
        self.boxSharpness.setGeometry(QtCore.QRect(140, 20, 71, 22))
        self.boxSharpness.setMinimum(-100)
        self.boxSharpness.setMaximum(100)
        self.boxSharpness.setSingleStep(1)
        self.boxSharpness.setObjectName(_fromUtf8("boxSharpness"))
        self.boxContrast = QtGui.QSpinBox(self.groupBox)
        self.boxContrast.setGeometry(QtCore.QRect(140, 60, 71, 22))
        self.boxContrast.setMinimum(-100)
        self.boxContrast.setMaximum(100)
        self.boxContrast.setSingleStep(1)
        self.boxContrast.setObjectName(_fromUtf8("boxContrast"))
        self.boxSaturation = QtGui.QSpinBox(self.groupBox)
        self.boxSaturation.setGeometry(QtCore.QRect(140, 140, 71, 22))
        self.boxSaturation.setMinimum(-100)
        self.boxSaturation.setMaximum(100)
        self.boxSaturation.setObjectName(_fromUtf8("boxSaturation"))
        self.boxBrightness = QtGui.QSpinBox(self.groupBox)
        self.boxBrightness.setGeometry(QtCore.QRect(140, 100, 71, 22))
        self.boxBrightness.setMaximum(100)
        self.boxBrightness.setSingleStep(1)
        self.boxBrightness.setObjectName(_fromUtf8("boxBrightness"))
        self.boxIso = QtGui.QSpinBox(self.groupBox)
        self.boxIso.setGeometry(QtCore.QRect(140, 180, 71, 22))
        self.boxIso.setMinimum(100)
        self.boxIso.setMaximum(800)
        self.boxIso.setSingleStep(100)
        self.boxIso.setObjectName(_fromUtf8("boxIso"))
        self.btnClear = QtGui.QPushButton(self.groupBox)
        self.btnClear.setGeometry(QtCore.QRect(50, 220, 101, 24))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 10, 281, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnAkt = QtGui.QPushButton(self.groupBox_2)
        self.btnAkt.setGeometry(QtCore.QRect(80, 220, 101, 24))
        self.btnAkt.setObjectName(_fromUtf8("btnAkt"))
        self.labLive = QtGui.QLabel(self.groupBox_2)
        self.labLive.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive.setObjectName(_fromUtf8("labLive"))
        self.btnClose = QtGui.QPushButton(self.tab_2)
        self.btnClose.setGeometry(QtCore.QRect(110, 270, 83, 24))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnAusl = QtGui.QPushButton(self.tab_2)
        self.btnAusl.setGeometry(QtCore.QRect(10, 270, 83, 24))
        self.btnAusl.setObjectName(_fromUtf8("btnAusl"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(260, 10, 281, 251))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.btnAkt_3 = QtGui.QPushButton(self.groupBox_6)
        self.btnAkt_3.setGeometry(QtCore.QRect(80, 220, 101, 24))
        self.btnAkt_3.setObjectName(_fromUtf8("btnAkt_3"))
        self.labLive_3 = QtGui.QLabel(self.groupBox_6)
        self.labLive_3.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive_3.setObjectName(_fromUtf8("labLive_3"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 10, 231, 81))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.boxPresets = QtGui.QComboBox(self.groupBox_7)
        self.boxPresets.setGeometry(QtCore.QRect(10, 40, 211, 22))
        self.boxPresets.setObjectName(_fromUtf8("boxPresets"))
        self.btnAusl_2 = QtGui.QPushButton(self.tab)
        self.btnAusl_2.setGeometry(QtCore.QRect(20, 100, 83, 24))
        self.btnAusl_2.setObjectName(_fromUtf8("btnAusl_2"))
        self.btnClose_3 = QtGui.QPushButton(self.tab)
        self.btnClose_3.setGeometry(QtCore.QRect(120, 100, 83, 24))
        self.btnClose_3.setObjectName(_fromUtf8("btnClose_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.btnStart = QtGui.QPushButton(self.tab_3)
        self.btnStart.setGeometry(QtCore.QRect(10, 230, 83, 24))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 221, 151))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.radioSec = QtGui.QRadioButton(self.groupBox_3)
        self.radioSec.setGeometry(QtCore.QRect(20, 60, 100, 19))
        self.radioSec.setChecked(True)
        self.radioSec.setObjectName(_fromUtf8("radioSec"))
        self.radioMin = QtGui.QRadioButton(self.groupBox_3)
        self.radioMin.setGeometry(QtCore.QRect(130, 60, 100, 19))
        self.radioMin.setObjectName(_fromUtf8("radioMin"))
        self.radioHour = QtGui.QRadioButton(self.groupBox_3)
        self.radioHour.setGeometry(QtCore.QRect(20, 80, 100, 19))
        self.radioHour.setObjectName(_fromUtf8("radioHour"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 119, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.boxZeitraum = QtGui.QSpinBox(self.layoutWidget)
        self.boxZeitraum.setObjectName(_fromUtf8("boxZeitraum"))
        self.horizontalLayout_2.addWidget(self.boxZeitraum)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 110, 121, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.boxAnzahl = QtGui.QSpinBox(self.layoutWidget1)
        self.boxAnzahl.setObjectName(_fromUtf8("boxAnzahl"))
        self.horizontalLayout.addWidget(self.boxAnzahl)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 170, 221, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btnClose_2 = QtGui.QPushButton(self.tab_3)
        self.btnClose_2.setGeometry(QtCore.QRect(100, 230, 83, 24))
        self.btnClose_2.setObjectName(_fromUtf8("btnClose_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 10, 281, 251))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.btnAkt_2 = QtGui.QPushButton(self.groupBox_4)
        self.btnAkt_2.setGeometry(QtCore.QRect(80, 220, 101, 24))
        self.btnAkt_2.setObjectName(_fromUtf8("btnAkt_2"))
        self.labLive_2 = QtGui.QLabel(self.groupBox_4)
        self.labLive_2.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive_2.setObjectName(_fromUtf8("labLive_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(260, 10, 281, 221))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.labLive_4 = QtGui.QLabel(self.groupBox_8)
        self.labLive_4.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive_4.setObjectName(_fromUtf8("labLive_4"))
        self.lab = QtGui.QLabel(self.tab_4)
        self.lab.setGeometry(QtCore.QRect(40, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab.setFont(font)
        self.lab.setObjectName(_fromUtf8("lab"))
        self.labTime = QtGui.QLabel(self.tab_4)
        self.labTime.setGeometry(QtCore.QRect(40, 90, 191, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labTime.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labTime.setFont(font)
        self.labTime.setText(_fromUtf8(""))
        self.labTime.setObjectName(_fromUtf8("labTime"))
        self.labDate = QtGui.QLabel(self.tab_4)
        self.labDate.setGeometry(QtCore.QRect(10, 190, 221, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labDate.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labDate.setFont(font)
        self.labDate.setText(_fromUtf8(""))
        self.labDate.setObjectName(_fromUtf8("labDate"))
        self.btnCamOn = QtGui.QPushButton(self.tab_4)
        self.btnCamOn.setGeometry(QtCore.QRect(30, 230, 83, 24))
        self.btnCamOn.setObjectName(_fromUtf8("btnCamOn"))
        self.btnClose_4 = QtGui.QPushButton(self.tab_4)
        self.btnClose_4.setGeometry(QtCore.QRect(450, 260, 83, 24))
        self.btnClose_4.setObjectName(_fromUtf8("btnClose_4"))
        self.btnCamOff = QtGui.QPushButton(self.tab_4)
        self.btnCamOff.setGeometry(QtCore.QRect(140, 230, 83, 24))
        self.btnCamOff.setObjectName(_fromUtf8("btnCamOff"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_9.setGeometry(QtCore.QRect(260, 10, 281, 251))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.btnAkt_4 = QtGui.QPushButton(self.groupBox_9)
        self.btnAkt_4.setGeometry(QtCore.QRect(80, 220, 101, 24))
        self.btnAkt_4.setObjectName(_fromUtf8("btnAkt_4"))
        self.labLive_5 = QtGui.QLabel(self.groupBox_9)
        self.labLive_5.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive_5.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive_5.setObjectName(_fromUtf8("labLive_5"))
        self.btnClose_5 = QtGui.QPushButton(self.tab_6)
        self.btnClose_5.setGeometry(QtCore.QRect(120, 100, 83, 24))
        self.btnClose_5.setObjectName(_fromUtf8("btnClose_5"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 10, 231, 80))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.label_9 = QtGui.QLabel(self.groupBox_10)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.boxEffects = QtGui.QComboBox(self.groupBox_10)
        self.boxEffects.setGeometry(QtCore.QRect(10, 40, 211, 22))
        self.boxEffects.setObjectName(_fromUtf8("boxEffects"))
        self.btnAusl_3 = QtGui.QPushButton(self.tab_6)
        self.btnAusl_3.setGeometry(QtCore.QRect(20, 100, 83, 24))
        self.btnAusl_3.setObjectName(_fromUtf8("btnAusl_3"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_11.setGeometry(QtCore.QRect(260, 10, 281, 251))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.btnAkt_5 = QtGui.QPushButton(self.groupBox_11)
        self.btnAkt_5.setGeometry(QtCore.QRect(80, 220, 101, 24))
        self.btnAkt_5.setObjectName(_fromUtf8("btnAkt_5"))
        self.labLive_6 = QtGui.QLabel(self.groupBox_11)
        self.labLive_6.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.labLive_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labLive_6.setObjectName(_fromUtf8("labLive_6"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 10, 231, 251))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.splitter = QtGui.QSplitter(self.groupBox_12)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 190, 221))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_10 = QtGui.QLabel(self.splitter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineWidth = QtGui.QLineEdit(self.splitter)
        self.lineWidth.setObjectName(_fromUtf8("lineWidth"))
        self.label_11 = QtGui.QLabel(self.splitter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineHeight = QtGui.QLineEdit(self.splitter)
        self.lineHeight.setObjectName(_fromUtf8("lineHeight"))
        self.label_12 = QtGui.QLabel(self.splitter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineRate = QtGui.QLineEdit(self.splitter)
        self.lineRate.setObjectName(_fromUtf8("lineRate"))
        self.label_13 = QtGui.QLabel(self.splitter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineTime = QtGui.QLineEdit(self.splitter)
        self.lineTime.setObjectName(_fromUtf8("lineTime"))
        self.label_14 = QtGui.QLabel(self.splitter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineFps = QtGui.QLineEdit(self.splitter)
        self.lineFps.setObjectName(_fromUtf8("lineFps"))
        self.btnStart_2 = QtGui.QPushButton(self.tab_5)
        self.btnStart_2.setGeometry(QtCore.QRect(20, 270, 83, 24))
        self.btnStart_2.setObjectName(_fromUtf8("btnStart_2"))
        self.btnClose_6 = QtGui.QPushButton(self.tab_5)
        self.btnClose_6.setGeometry(QtCore.QRect(120, 270, 83, 24))
        self.btnClose_6.setObjectName(_fromUtf8("btnClose_6"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
 
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 571, 19))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuEinstellungen = QtGui.QMenu(self.menuBar)
        self.menuEinstellungen.setObjectName(_fromUtf8("menuEinstellungen"))

        self.actionSpeicherort = QtGui.QAction(MainWindow)
        self.actionSpeicherort.setObjectName(_fromUtf8("actionSpeicherort"))
        self.menuEinstellungen.addAction(self.actionSpeicherort)
        self.menuBar.addAction(self.menuEinstellungen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PinQam", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Sättigung", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Kontrast", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Schärfe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Helligkeit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MainWindow", "Zurücksetzen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Live-View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAkt.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive.setText(QtGui.QApplication.translate("MainWindow", "Bitte aktualisieren!", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAusl.setText(QtGui.QApplication.translate("MainWindow", "Auslösen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Manuell", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Live-View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAkt_3.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive_3.setText(QtGui.QApplication.translate("MainWindow", "Bitte aktualisieren!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Belichtung", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Voreinstellung wählen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAusl_2.setText(QtGui.QApplication.translate("MainWindow", "Auslösen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose_3.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Motivprogramme", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSec.setText(QtGui.QApplication.translate("MainWindow", "Sekunden", None, QtGui.QApplication.UnicodeUTF8))
        self.radioMin.setText(QtGui.QApplication.translate("MainWindow", "Minuten", None, QtGui.QApplication.UnicodeUTF8))
        self.radioHour.setText(QtGui.QApplication.translate("MainWindow", "Stunden", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Zeitraum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Bilderzahl", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Fortschritt", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose_2.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Live-View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAkt_2.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive_2.setText(QtGui.QApplication.translate("MainWindow", "Bitte aktualisieren!", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Zeitraffer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", "Webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive_4.setText(QtGui.QApplication.translate("MainWindow", "Webcam ist ausgeschaltet!", None, QtGui.QApplication.UnicodeUTF8))
        self.lab.setText(QtGui.QApplication.translate("MainWindow", "letztes Foto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCamOn.setText(QtGui.QApplication.translate("MainWindow", "Einschalten", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose_4.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCamOff.setText(QtGui.QApplication.translate("MainWindow", "Ausschalten", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("MainWindow", "Live-View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAkt_4.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive_5.setText(QtGui.QApplication.translate("MainWindow", "Bitte aktualisieren!", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose_5.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Filer wählen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAusl_3.setText(QtGui.QApplication.translate("MainWindow", "Auslösen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Filtereffekte", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("MainWindow", "Live-View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAkt_5.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.labLive_6.setText(QtGui.QApplication.translate("MainWindow", "Bitte aktualisieren!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("MainWindow", "Konfiguration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Breite (min 64px  max 1920px)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Höhe (min 64px  max 1080px)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Bitrate in MBit/s (H264 = 10)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Aufnahmedauer in s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "FPS (min 2 max 30)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart_2.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose_6.setText(QtGui.QApplication.translate("MainWindow", "Schliesen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Video", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEinstellungen.setTitle(QtGui.QApplication.translate("MainWindow", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeicherort.setText(QtGui.QApplication.translate("MainWindow", "Speicherort auswählen", None, QtGui.QApplication.UnicodeUTF8))

