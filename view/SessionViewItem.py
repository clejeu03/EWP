#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SessionViewItem(QtGui.QWidget):
    """
    This class define the item contained in the SessionView that stands for videos. An item is composed by a thumbnail of the video,
    the name of the video and the duration of the video. it has a contextual menu and a special double click event that enable the user
    to play the selected video.
    """
    def __init__(self, video, parent=None):
        super(SessionViewItem, self).__init__()

        self.parent = parent
        self.video = video

        #For css naming
        self.setObjectName("ItemWidget")

        self.createContextMenu()
        self.init()


    def init(self):
        """ Draw tha main layout   """

        layout = QtGui.QHBoxLayout()

        #Draw the snapshot
        picture = self.drawThumbnail()
        layout.addWidget(picture)

        #Display the title
        title = QtGui.QLabel(self.video.getName())
        layout.addWidget(title)

        #Display the duration of the video
        duration = QtGui.QLabel(self.video.computeDuration())
        layout.addWidget(duration)

        #Set spacing
        layout.setStretchFactor(picture, 2)
        layout.setStretchFactor(title, 4)
        layout.setStretchFactor(duration, 1)

        self.setLayout(layout)

    def createContextMenu(self):
        """ Creates the actions and set the widget for displaying a context menu at right click event  """

        #Enabling the context menu with actions
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        #Creation of a context menu action to suppress the clicked self
        suppressAction = QtGui.QAction(self.tr("&Delete"), self)
        suppressAction.setStatusTip(self.tr("Remove the video from the project"))
        self.connect(suppressAction, QtCore.SIGNAL("triggered()"), self.parent, QtCore.SLOT("suppressVideo()"))
        self.addAction(suppressAction)

        #Creation of the play video action
        playAction = QtGui.QAction(self.tr("&Play"), self)
        playAction.setStatusTip(self.tr("Play this video in a new window"))
        self.connect(playAction, QtCore.SIGNAL("triggered()"), self.parent, QtCore.SLOT("playVideo()"))
        self.addAction(playAction)

    def drawThumbnail(self):
        """
        Extract a thumbnail from the video and return it
        :return : QPixmap
        """
        thumbnail = QtGui.QPixmap(self.video.getThumbnail())
        reduceThumbnail = thumbnail.scaledToHeight(30)
        picture = QtGui.QLabel()
        picture.setPixmap(reduceThumbnail)

        return picture

    def mouseDoubleClickEvent(self, *args, **kwargs):
        """Override the mouse double click event """
        self.parent.playVideo()

