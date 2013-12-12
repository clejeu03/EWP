#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import cv2
import numpy as np
from view.PlayerSlider import PlayerSlider

class Player(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Player, self).__init__()

        self.parent = parent

        self.video = None
        self.slider = QtGui.QSlider()
        self.title = None
        self.capture = None
        self.playStatus = False
        self.label = QtGui.QLabel()
        self.timerId = None


    def init(self):
        """ Draw the layout of the widget and prepare the video  """

        self.setWindowTitle(self.video.getName())
        layout  = QtGui.QVBoxLayout()

        #Create a capture from the video
        self.capture = cv2.VideoCapture(self.video.getPath())
        value, frame = self.capture.read()

        #Show the first frame of the video
        if value:
            self.showFrame(frame)

        layout.addWidget(self.label)

        #The controls are composed of the play/pause button, of the slider and of a time label
        controlLayout = QtGui.QHBoxLayout()

        #Button Play/Pause
        playPauseButton = QtGui.QPushButton("play / pause ")
        playPauseButton.setFixedWidth(30)
        self.connect(playPauseButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("playPauseTrigger()"))
        controlLayout.addWidget(playPauseButton)

        #Slider
        self.slider = PlayerSlider(self)
        self.slider.setRange(0, self.video.getDuration())
        self.connect(self.slider, QtCore.SIGNAL("newValue(int)"), self, QtCore.SLOT("updateFramePos(int)"))
        self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"), self, QtCore.SLOT("displayTime(int)"))
        controlLayout.addWidget(self.slider)

        #Time
        self.currentTimeLabel = QtGui.QLabel()
        self.displayTime(0)
        totalTimeLabel = QtGui.QLabel(" / " + self.video.computeDuration())
        controlLayout.addWidget(self.currentTimeLabel)
        controlLayout.addWidget(totalTimeLabel)

        layout.addLayout(controlLayout)

        self.setLayout(layout)

        #Display the player in the center of the screen
        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())

    def displayTime(self, value):
        """
        Take the value given, normaly connected to the slider value, and transform it into seconds to compute the actual video time position
        :param value : the position of the slider = the number of seconds the video have been played for
        :type value: int
        """
        origin = QtCore.QTime(0, 0, 0)

        #updating the current time following the given value
        currentTime = origin.addSecs(value)

        #Adapting the display to the duration
        if self.video.getDuration() < 3600: #seconds
            self.currentTimeLabel.setText(currentTime.toString("mm:ss"))
        else:
            self.currentTimeLabel.setText(currentTime.toString())


    @QtCore.Slot(int)
    def updateFramePos(self, value):
        """
        Update the position of the video following the position of the slider
        :param value : the position of the slider
        :type value: int
        """
        self.capture.set(0,value*1000)
        self.displayTime(value)

    def showFrame(self, frame):
        """ This function must be call regularly in order to update the video frame currently shown  """
        qImage = self.toQImage(frame)
        pixmap = QtGui.QPixmap().fromImage(qImage)
        self.label.setPixmap(pixmap)
        pos = self.capture.get(0) #milliseconds

        #Update the slider
        newPos = QtCore.qRound(pos/1000)
        if self.slider.value() != newPos:
            self.slider.setValue(newPos)

    def start(self, video):
        """ Start a new window to play the selected video  """
        self.video = video
        self.show()
        self.init()
        self.playPauseTrigger()

    def playPauseTrigger(self):
        """ Manage the play and pause of the video following the value of the playStatus boolean   """

        #If the video is currently paused...
        if self.playStatus is False:
            self.playStatus = True
            self.timerId = self.startTimer(41.666)

        #If the video is currently playing...
        else:
            self.playStatus = False
            self.killTimer(self.timerId)

    # --------------------------- EVENT HANDLERS ---------------------------- #
    def closeEvent(self, event):
        """ On close event, the timer must stop if it's not already  """
        if not self.timerId is None:
            self.killTimer(self.timerId)

    def timerEvent(self, event):
        """ Override the QObject method to call a function periodically """
        value, frame = self.capture.read()
        if value:
            self.showFrame(frame)

    # --------------------------- CONVERSIONS FUNCTION --------------------------- #
    def toQImage(self, im, copy=False):
        """ Conversion from a numpy array to a QImage """
        if im is None:
            return QtGui.QImage()

        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        if im.dtype == np.uint8 and len(im.shape) == 3:
            qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888)
            return qim.rgbSwapped().copy() if copy else qim.rgbSwapped()
        elif im.dtype == np.uint8 and len(im.shape) == 1:
            qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim.copy() if copy else qim
        else :
            raise RuntimeError("Player : cannot convert frame to QImage.")
