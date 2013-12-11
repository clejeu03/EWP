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
        self.label = None


    def init(self):
        """ Draw the layout of the widget and prepare the video  """

        #The controls ares composed of the play/pause button and of the slider
        controlLayout = QtGui.QHBoxLayout()

        #The video view
        capture = cv2.VideoCapture(self.video.getPath())

        self.label = QtGui.QLabel()
        value, frame = capture.read()
        print "value : " + str(value)
        while value:
            self.showFrame(frame)
            count = capture.get(1)
            print "count : " + str(count)
            value, frame = capture.read()

        layout  = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        #layout.addLayout(controlLayout)

        self.setLayout(layout)
        self.playStatus = True


    def showFrame(self, frame):
        """ This function must be call regurlarly in order to update the video frame currently shown  """

        qImage = self.toQImage(frame)
        pixmap = QtGui.QPixmap().fromImage(qImage)
        self.label.setPixmap(pixmap)

    def timerEvent(self, *args, **kwargs):
        """ Override the QObject method to call a function periodically """
        value, frame = self.capture.read()
        if value:
            self.showFrame(frame)
            count = self.capture.get(1)
            print "count : " + str(count)

    def play(self, video):
        """ Start a new window to play the selected video  """
        self.video = video
        self.init()
        #self.timerId = self.startTimer(41.666)
        self.show()

    def pause(self):
        pass

    # --------------------------- CONVERSIONS FUNCTION --------------------------- #
    def toQImage(self, im, copy=False):
        """ Conversion from a numpy array to a QImage """
        if im is None:
            return QtGui.QImage()

        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888);
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_ARGB32);
                    return qim.copy() if copy else qim
