#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.Track import Track

class SketchBoardView (QtGui.QWidget):

    def __init__(self, app):
        super(SketchBoardView, self).__init__()

        self._app = app
        self._model = app.getSession().currentProject()

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
        widget = Track(video)
        self._videoListView.append(widget)

    def update(self):
        pass
