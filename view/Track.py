#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class Track (QtGui.QListWidgetItem):

    def __init__(self, video):
        super(Track, self).__init__()

        self._video = video
        self._mode = 'DEFAULT'
        #TODO : enum ?

    def init(self):
        layout = QtGui.QHBoxLayout()
        videoName = QtGui.QLabel(self._video.getName())

        #self.drawTrack(self._video)

        layout.addWidget(videoName)

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
