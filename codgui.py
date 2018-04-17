# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codgui.ui'
#
# Created: Thu Dec 18 20:05:59 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 303)
        self.playButton = QtGui.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.playButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../unnamed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(70, 10, 21, 21))
        self.stopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../002116-glossy-black-3d-button-icon-media-a-media28-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.pauseButton = QtGui.QPushButton(Form)
        self.pauseButton.setGeometry(QtCore.QRect(40, 10, 21, 21))
        self.pauseButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.volumeSlider = QtGui.QSlider(Form)
        self.volumeSlider.setEnabled(True)
        self.volumeSlider.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.songListWidget = QtGui.QListWidget(Form)
        self.songListWidget.setGeometry(QtCore.QRect(10, 60, 381, 231))
        self.songListWidget.setObjectName(_fromUtf8("songListWidget"))
        self.songInfoFrame = QtGui.QFrame(Form)
        self.songInfoFrame.setGeometry(QtCore.QRect(120, 10, 251, 41))
        self.songInfoFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.songInfoFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.songInfoFrame.setObjectName(_fromUtf8("songInfoFrame"))
        self.seekSlider = QtGui.QSlider(self.songInfoFrame)
        self.seekSlider.setGeometry(QtCore.QRect(40, 20, 211, 21))
        self.seekSlider.setMouseTracking(True)
        self.seekSlider.setTracking(False)
        self.seekSlider.setOrientation(QtCore.Qt.Horizontal)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.label = QtGui.QLabel(self.songInfoFrame)
        self.label.setGeometry(QtCore.QRect(70, 10, 141, 20))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.songName = QtGui.QLabel(self.songInfoFrame)
        self.songName.setGeometry(QtCore.QRect(120, 10, 71, 16))
        self.songName.setObjectName(_fromUtf8("songName"))
        self.shuffleButton = QtGui.QPushButton(self.songInfoFrame)
        self.shuffleButton.setGeometry(QtCore.QRect(10, 0, 21, 20))
        self.shuffleButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../button_shuffle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffleButton.setIcon(icon3)
        self.shuffleButton.setObjectName(_fromUtf8("shuffleButton"))
        self.repeatButton = QtGui.QPushButton(self.songInfoFrame)
        self.repeatButton.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.repeatButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../007761-glossy-black-3d-button-icon-arrows-arrows1-shuffle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatButton.setIcon(icon4)
        self.repeatButton.setObjectName(_fromUtf8("repeatButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.songName.setText(_translate("Form", "TextLabel", None))

