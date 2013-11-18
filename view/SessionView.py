#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SessionView(QtGui.QWidget) :

    def __init__(self, controller):
        super(SessionView, self).__init__()

        self.controller = controller
        self.list = None

        self.init()

    def init(self):
        """ Draw the session view for the first time """
        self.list = QtGui.QListWidget()

        #If the project is not null, then we draw the video it contains
        if not self.controller.getSession().currentProject() is None:
            for video in self.controller.getSession().currentProject().getVideos():
                self.list.addItem(video.getListWidget())

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.list)
        self.setLayout(layout)

    def update(self):
        """ Update the view with the model data"""
        pass


