#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class Track (QtGui.QListWidgetItem):

    def __init__(self, video):
        super(Track, self).__init__()

        self._video = video
        self._mode = 'DEFAULT'

        self.setText(self._video.getName())


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
