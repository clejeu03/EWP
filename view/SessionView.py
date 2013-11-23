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

        layout = QtGui.QVBoxLayout()

        #If the project is not null, then we draw the video it contains
        if not self.controller.getSession().currentProject() is None:

            self.list = QtGui.QListWidget()

            for video in self.controller.getSession().currentProject().getVideos():
                #Prepare the view of each item in the project
                listItem = self.drawListItemView(video)
                self.list.addItem(listItem)

            #Draw the title of the project
            title = QtGui.QLabel(self.controller.getSession().currentProject().getName())
            layout.addWidget(title)

            #Draw the elements of the project
            layout.addWidget(self.list)

        #Display a message to tell the user project is missing
        else:
            missingLabel = QtGui.QLabel("There is no project. Please create or open one.")
            layout.addWidget(missingLabel)
        self.setLayout(layout)

    def drawListItemView(self, video):
        """
        This function create the ListItemWidget contained by the ListViewWidget of the SessionView
        :param video: the video targeted in the current project
        :type video: class Video
        :return type: QListWidgetItem
        """
        item = QtGui.QListWidgetItem()
        item.setText(video.getName())

        #layout = QtGui.QHBoxLayout()

        thumbnail = QtGui.QPixmap(video.getThumbnail())
        item.setIcon(thumbnail)

        #layout.addWidget(thumbnail)
        #item.setLayout(layout)

        return item

    def update(self):
        """ Update the view with the model data"""
        pass


