#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import math

class SessionView(QtGui.QWidget) :

    def __init__(self, controller):
        super(SessionView, self).__init__()

        self._controller = controller
        self.list = None

        self.init()

    def init(self):
        """ Draw the session view for the first time """

        self.layout = QtGui.QVBoxLayout()

        if not self._controller.getSession().currentProject() is None:
            self.list = self.update()

            #Draw the elements of the project
            self.layout.addWidget(self.list)

        else:
            #Display a message to tell the user project is missing
            missingLabel = QtGui.QLabel("There is no project. Please create or open one.")
            self.layout.addWidget(missingLabel)

        self.setLayout(self.layout)

    def drawListItemWidget(self, video):
        """
        This function create the ListItemWidget contained by the ListViewWidget of the SessionView
        :param video: the video targeted in the current project
        :type video: class Video
        :return type: QListWidgetItem
        """
        item = QtGui.QWidget()
        item.setObjectName("ItemWidget")

        #Enabling the context menu with actions
        item.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        #Creation of a context menu action to suppress the clicked item
        suppressAction = QtGui.QAction(self.tr("&Delete"), self)
        suppressAction.setStatusTip(self.tr("Remove the video from the project"))
        self.connect(suppressAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("suppressVideo()"))
        item.addAction(suppressAction)

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
        duration = QtGui.QLabel(video.computeDuration())
        layout.addWidget(duration)

        #Set spacing
        layout.setStretchFactor(picture, 2)
        layout.setStretchFactor(title, 4)
        layout.setStretchFactor(duration, 1)

        item.setLayout(layout)

        return item

    def suppressVideo(self):
        """ This function calls the controller function to suppress physically the video from the project directory nd to clean up the project data"""

        #Retrieve the current selected item of the session view.
        video = self.list.currentItem().data(QtCore.Qt.UserRole)
        self._controller.suppressVideo(video)

    def update(self):
        """ Update the view with the model data"""

        #TODO : check if the order of the video in the view is different before and after updating

        list = QtGui.QListWidget()

        #If the project is not null, then we draw the video it contains
        if not self._controller.getSession().currentProject() is None:
            #Draw the title of the project
            title = QtGui.QLabel(self._controller.getSession().currentProject().getName())
            self.layout.addWidget(title)

            #TODO : suppress the temporary text in the place of the list

            #Clear the view by erasing all the items of the list
            if not self.list is None:
                self.list.clear()

            #Create items according to those contained in the Project data
            for video in self._controller.getSession().currentProject().getVideos():
                #Prepare the view of each item in the project
                listItem = QtGui.QListWidgetItem()
                listItem.setData(QtCore.Qt.UserRole, video)
                itemWidget = self.drawListItemWidget(video)
                list.addItem(listItem)
                list.setItemWidget(listItem, itemWidget)

        return list


