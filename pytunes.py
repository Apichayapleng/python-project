from PySide.QtUiTools import QUiLoader
from PySide.QtGui import*
from PySide.phonon import Phonon
import sys

class MainMenu:
    def __init__(self):
        loader = QUiLoader()
        self.ui = loader.load('mainmenu.ui')
        self.ui.show()
        self.mapUi()

    def mapUi(self):
        self.AudioLink = self.ui.findChild(QPushButton, "AudioLink")
        self.AudioLink.clicked.connect(self.Alink)
        self.VideoLink = self.ui.findChild(QPushButton, "VideoLink")
        self.VideoLink.clicked.connect(self.Vlink)
        self.exitButton = self.ui.findChild(QPushButton, "exitButton")
        self.exitButton.clicked.connect(self.exitlink)

    def Alink(self):
        self.audio = PyTunes()
        self.audio.show()
        self.ui.close()

    def Vlink(self):
        self.ui.video = videoPlayer()
        self.ui.video.show()
        self.ui.close()

    def exitlink(self):
        exit()

    def show(self):
        self.ui.show()

class videoPlayer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Video Player')

        self.media = Phonon.MediaObject(self)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(400, 400)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        self.buttonChoose = QPushButton('Choose File', self)

        self.slider = Phonon.VolumeSlider(self)
        self.slider.setAudioOutput(self.audio)
        layout = QGridLayout(self)
        layout.addWidget(self.video, 0, 0, 1, 2)
        layout.addWidget(self.buttonChoose, 1, 0)

        layout.addWidget(self.slider, 2, 0, 1, 2)
        layout.setRowStretch(0, 1)
        self.media.stateChanged.connect(self.handleStateChanged)
        self.buttonChoose.clicked.connect(self.handleButtonChoose)


    def handleButtonChoose(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.ExistingFile)
            if dialog.exec_() == QDialog.Accepted:
                path = dialog.selectedFiles()[0]
                self.media.setCurrentSource(Phonon.MediaSource(path))
                self.media.play()
            dialog.deleteLater()

    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.buttonChoose.setText('Stop')
        elif (newstate != Phonon.LoadingState and
              newstate != Phonon.BufferingState):
            self.buttonChoose.setText('Choose File')
            if newstate == Phonon.ErrorState:
                source = self.media.currentSource().fileName()
                print ('ERROR: could not play: %s' % source)
                print ('  %s' % self.media.errorString())

class PyTunes:
    def __init__(self):
        loader = QUiLoader()
        self.ui = loader.load('codegui.ui')
        self.mapUi()
        self.initPhonon()

    def mapUi(self):
        self.songlist = []
        self.playButton = self.ui.findChild(QPushButton, "playButton")
        self.playButton.clicked.connect(self.play)
        self.pauseButton = self.ui.findChild(QPushButton, "pauseButton")
        self.pauseButton.clicked.connect(self.pause)
        self.stopButton = self.ui.findChild(QPushButton, "stopButton")
        self.stopButton.clicked.connect(self.stop)
        self.volumeSlider = self.ui.findChild(QSlider, "volumeSlider")
        self.volumeSlider.valueChanged.connect(self.changeVolume)

        self.songInfoFrame = self.ui.findChild(QFrame, "songInfoFrame")
        self.songName = self.ui.findChild(QLabel, "songName")

        self.songListWidget = self.ui.findChild(QListWidget, "songListWidget")
        self.songListWidget.itemDoubleClicked.connect(self.selectSong)
        # self.songListWidget.itemClicked.connect(self.selectSong)

        self.addAudioFiles = self.ui.findChild(QPushButton, "addAudioFiles")
        self.addAudioFiles.clicked.connect(self.addAudio)
        # self.volumeSlider.setMaximum(20)

        self.Menulink = self.ui.findChild(QPushButton, "Menulink")
        self.Menulink.clicked.connect(self.backMenu)
        self.exitButton = self.ui.findChild(QPushButton, "exitButton")
        self.exitButton.clicked.connect(self.exitlink)

    def initPhonon(self):
        self.media = Phonon.MediaObject(self.ui)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self.ui)
        Phonon.createPath(self.media, self.audio)

    def backMenu(self):
        self.menu = MainMenu()
        self.menu.show()
        self.ui.close()

    def show(self):
        self.ui.show()

    def changeVolume(self):
        volume = self.volumeSlider.value()
        # print("volume:", volume)
        self.audio.setVolume(volume)

    def addAudio(self):
        dialog = QFileDialog(self.ui)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        if dialog.exec_() == QDialog.Accepted:
            paths = dialog.selectedFiles()
            for path in paths:
                name = path.split("/")[-1]
                self.songListWidget.addItem(name)
                self.songlist.append(path)
        dialog.deleteLater()

    def play(self):
        self.media.play()

    def pause(self):
        self.media.pause()

    def stop(self):
        self.media.stop()

    def selectSong(self, list):
        self.media.setCurrentSource(Phonon.MediaSource(list.text()))
        name = list.text().split("/")[-1]
        print("showing: ", name)
        self.songName.setText(name)
        self.media.play()

    def exitlink(self):
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)      # open application
    menu = MainMenu()

    app.exec_()