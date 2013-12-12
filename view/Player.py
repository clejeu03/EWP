#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import cv2
import numpy as np

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


    def init(self):
        """ Draw the layout of the widget and prepare the video  """

        layout  = QtGui.QVBoxLayout()

        #Create a capture from the video
        self.capture = cv2.VideoCapture(self.video.getPath())
        value, frame = self.capture.read()

        #Show the first frame of the video
        if value:
            self.showFrame(frame)

        layout.addWidget(self.label)

        #The controls are composed of the play/pause button and of the slider
        #controlLayout = QtGui.QHBoxLayout()
        #layout.addLayout(controlLayout)

        self.setLayout(layout)
        self.playStatus = True

    def showFrame(self, frame):
        """ This function must be call regularly in order to update the video frame currently shown  """
        qImage = self.toQImage(frame)
        pixmap = QtGui.QPixmap().fromImage(qImage)
        self.label.setPixmap(pixmap)

    def play(self, video):
        """ Start a new window to play the selected video  """
        self.video = video
        self.show()
        self.init()
        self.timerId = self.startTimer(41.666)

    def pause(self):
        pass

    # --------------------------- EVENT HANDLERS ---------------------------- #
    def closeEvent(self, event):
        """ On close event, the timer must stop if it's not already  """
        self.killTimer(self.timerId)

    def timerEvent(self, event):
        """ Override the QObject method to call a function periodically """
        value, frame = self.capture.read()
        if value:
            self.showFrame(frame)
            count = self.capture.get(1)

    # --------------------------- CONVERSIONS FUNCTION --------------------------- #
    def toQImage(self, im, copy=False):
        """ Conversion from a numpy array to a QImage """
        if im is None:
            return QtGui.QImage()

        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        if im.dtype == np.uint8 and len(im.shape) == 3:
            print 'plop3'
            qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888)
            return qim.rgbSwapped().copy() if copy else qim.rgbSwapped()
        elif im.dtype == np.uint8 and len(im.shape) == 1:
            print 'plop1'
            qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim.copy() if copy else qim
        else :
            raise RuntimeError("Player : cannot convert frame to QImage.")