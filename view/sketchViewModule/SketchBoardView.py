#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.sketchViewModule.Track import Track
from view.sketchViewModule.SketchList import SketchList

class SketchBoardView (QtGui.QWidget):

    def __init__(self, app, sessionView):
        super(SketchBoardView, self).__init__()

        self._app = app
        self._model = app.getSession().currentProject()
        self._sessionView = sessionView

        self._toolbar = None
        self._trackList = None
        self._stackedWidget = None

        self._videoTrackTable = {}

        self.init()

    def init(self):
        """ Initialize the widget   """
        #Init the toolbar
        self._toolbar = self.initToolbar()

        #Init the main widget : the list
        self._trackList = SketchList()

        #Setting up the layout
        layout = QtGui.QVBoxLayout()
        self._stackedWidget = QtGui.QStackedWidget()
        self._stackedWidget.addWidget(self.createEmptyProjectWidget())
        self._stackedWidget.addWidget(self._trackList)

        #If there are no track then help the user by displaying special widget
        if self._trackList.count() == 0 :
            self._stackedWidget.setCurrentIndex(0)
        else:
            self._stackedWidget.setCurrentIndex(1)

        layout.addWidget(self._toolbar)
        layout.addWidget(self._stackedWidget)
        self.setLayout(layout)

    def initToolbar(self):
        """
        Creates the toolbar and the actions that goes in it, in addition make the necessary connection
        :return type: QToolbar
        """
        toolbar = QtGui.QToolBar()

        #Actions
        self.addVideoAction = QtGui.QAction(self.tr("&Add Video"), self)
        self.addVideoAction.setStatusTip(self.tr("Add a video to the sketch board"))
        #self.addVideoAction.setDisabled()
        self.connect(self.addVideoAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("addVideo()"))

        toolbar.addAction(self.addVideoAction)

        return toolbar

    def createEmptyProjectWidget(self):
        """ Creates a widget just for displaying instructions and help for the user in case the model data are empty """
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()

        label = QtGui.QLabel("Drag and drop a video from your project in here to add it ! ")

        layout.addWidget(label)
        widget.setLayout(layout)
        return widget

    def newTrack(self, video):
        """
        This function creates a line into the sketchboard view corresponding to a video
        :param video: the video that the sketch line stands for
        :type video: Video class from core module
        """
        #Updating the model
        self._model.newSketchBoardVideo(video)

        #Updating the view
        self.update()

    def update(self):
        """ Update the view of the list of tracks """

        #If the view got no tracks
        if self._trackList.count() == 0:
            self._stackedWidget.setCurrentIndex(0)

        #If the view already got tracks, just created new ones, and update the others
        else :
            for video in self._model.getSketchBoardVideos():

                if self._videoTrackTable.has_key(video):
                    #Retrieve all the values corresponding for the key
                    for widget in self._videoTrackTable.values():
                        #Update them only if there are different from the model data
                        if widget.getVideo() != video:
                            widget.update(video)
                else :
                    #Create a new track for this video
                    widget = Track(video)
                    item = QtGui.QListWidgetItem()
                    self._trackList.addItem(item)
                    self._trackList.setItemWidget(item, widget)

            self._stackedWidget.setCurrentIndex(1)

    # ----------------------- SIGNAL / SLOT ----------------------------------- #
    def addVideo(self):
        """ Retrieve the currently selected video from the session view to add it directly as a track """
        video = self._sessionView.getList().currentItem().data(QtCore.Qt.UserRole)
        self.newTrack(video)
