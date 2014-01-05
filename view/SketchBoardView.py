#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.VideoSketchView import VideoSketchView

class SketchBoardView (QtGui.QWidget):

    def __init__(self):
        super(SketchBoardView, self).__init__()

        self._toolbar = None
        self._videoListView = None

        #TODO : make a dict that associate a widget with its video ?

    def init(self):
        #TODO
        self._toolbar = QtGui.QToolBar()
        self._videoListView = QtGui.QListWidget()

    def addVideo(self, video):
        """
        Thisfunction creates a line into the sketchboard view corresponding to a video
        :param video: the video that the sketch line stands for
        :type video: Video class from core module
        """
        widget = VideoSketchView(video)
        self._videoListView.append(widget)

    def update(self):
        pass
