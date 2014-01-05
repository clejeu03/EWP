#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class Track (QtGui.QWidget):

    def __init__(self, video):
        super(Track, self).__init__()

        self._video = video
        self._mode = 'DEFAULT'

        #Graphics
        self._label = None
        self._scriptWitness = None
        self._reverseState = None
        self._drawPart = None

        self.init()

    def init(self):
        """Initialize the view of the widget """

        layout = QtGui.QHBoxLayout()

        #Set the script witness
        self._scriptWitness = QtGui.QPixmap(10, 30)
        self._scriptWitness.fill(QtCore.Qt.blue)
        scriptColor = QtGui.QLabel()
        scriptColor.setPixmap(self._scriptWitness)

        #Video title
        self._label = QtGui.QLabel(self._video.getName())

        #Main widget : the draw part
        self._drawPart = QtGui.QSlider()

        #Options
        self._reverseState = QtGui.QCheckBox()
        self._reverseState.setCheckState(QtCore.Qt.Unchecked)

        layout.addWidget(scriptColor)
        layout.addWidget(self._label)
        layout.addWidget(self._drawPart)
        layout.addWidget(self._reverseState)
        self.setLayout(layout)

    def drawTrack(self):
        """
        Draw the track under the appropriate shape referenced under "mode".
        :rtype: QWidget
        :return: the widget
        """
        if self._mode == 'DEFAULT':
            #Draw the track under the view of a "slider"
            slider = QtGui.QSlider()
            slider.setRange(0, self._video.getDuration())

            return slider

        else :
            raise RuntimeError("Plop error ! ")
