#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui
import math

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
                listItem = QtGui.QListWidgetItem()
                itemWidget = self.drawListItemWidget(video)
                self.list.addItem(listItem)
                self.list.setItemWidget(listItem, itemWidget)

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

    def drawListItemWidget(self, video):
        """
        This function create the ListItemWidget contained by the ListViewWidget of the SessionView
        :param video: the video targeted in the current project
        :type video: class Video
        :return type: QListWidgetItem
        """
        item = QtGui.QWidget()
        item.setObjectName("ItemWidget")

        layout = QtGui.QHBoxLayout()

        #Draw the snapshot
        thumbnail = QtGui.QPixmap(video.getThumbnail())
        reduceThumbnail = thumbnail.scaledToHeight(30)
        picture = QtGui.QLabel()
        picture.setPixmap(reduceThumbnail)
        layout.addWidget(picture)

        #Display the title
        title = QtGui.QLabel(video.getName())
        layout.addWidget(title)

        #Display the duration of the video
        minutes = math.trunc(math.floor(video.getDuration() / 60))
        seconds = math.trunc(video.getDuration() - minutes*60)
        duration = QtGui.QLabel(str(minutes) + ":" + str(seconds))
        if minutes > 60 : #Just in case a video is very long...
            hours = math.trunc(math.floor(minutes / 60))
            minutes = math.trunc(minutes - (hours*60))
            seconds = math.trunc(video.getDuration() - minutes*60)
            duration = QtGui.QLabel(str(hours) + ":" + str(minutes) + ":" + str(seconds))
        layout.addWidget(duration)

        item.setLayout(layout)

        return item

    def update(self):
        """ Update the view with the model data"""
        pass


