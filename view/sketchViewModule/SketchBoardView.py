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

        self.setAcceptDrops(True)

        self._toolbar = None
        self._trackList = None
        self._stackedWidget = None

        self._videoTrackTable = {}
        # /!\ Note : self._videoTrackTable stands for a dict where the keys are the widget contained in QListWidgetItem and the values
        # are the video that were used for the widget creation. Why ? Because each widget is unique whereas a video can be found multiple
        # times in the container. So as in Python dict contain unique key, THE WIDGETS ARE THE KEYS

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

        layout.addWidget(self._toolbar)
        layout.addWidget(self._stackedWidget)
        self.setLayout(layout)

        #Display tracks if there are, or the empty widget
        self.update()

    def initToolbar(self):
        """
        Creates the toolbar and the actions that goes in it, in addition make the necessary connection
        :return type: QToolbar
        """
        toolbar = QtGui.QToolBar()

        #TODO : manage the enable/desable of the actions

        #Actions
        self.addVideoAction = QtGui.QAction(self.tr("&Add Video"), self)
        self.addVideoAction.setStatusTip(self.tr("Add a video to the sketch board"))
        #self.addVideoAction.setDisabled()
        self.connect(self.addVideoAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("addVideo()"))

        self.suppressVideoAction = QtGui.QAction(self.tr("&Remove Video"), self)
        self.suppressVideoAction.setStatusTip(self.tr("Remove the selected video from the sketch board"))
        #self.suppressVideoAction.setDisabled()
        self.connect(self.suppressVideoAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("suppressVideo()"))

        toolbar.addAction(self.addVideoAction)
        toolbar.addAction(self.suppressVideoAction)

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

    def removeTrack(self, track):
        """
        This function calls the model and remove the video corresponding to the selected track.
        :param track : the track selected in the view
        :type track: QListWidgetItem
        """
        #Retrieve the widget
        widget = self._trackList.itemWidget(track)
        video = widget.getVideo()

        #Send to the model
        self._model.removeSketchBoardVideo(video)

        #Updating the view
        self.update()

    def update(self):
        """ Update the view of the list of tracks """

        #If the view got no tracks
        if len(self._model.getSketchBoardVideos()) == 0:
            self._stackedWidget.setCurrentIndex(0)

        #If the view already got tracks, just created new ones, and update the others
        else :
            for video in self._model.getSketchBoardVideos():

                if video in self._videoTrackTable.values():
                    #Updating the data from the model
                    #Retrieve all the keys corresponding for the value
                    # for key in self._videoTrackTable.keys():
                    #     #Update them only if there are different from the model data
                    #     if self._videoTrackTable[key] == video:
                    #         if  key.getVideo() != video:
                    #             key.update(video)
                    pass
                else :
                    #Create a new track for this video
                    widget = Track(video)
                    item = QtGui.QListWidgetItem()
                    self._trackList.addItem(item)
                    self._trackList.setItemWidget(item, widget)
                    #Reference the new variables
                    self._videoTrackTable[widget] = video

            #Check if a video have been suppressed
            for widget, video in  self._videoTrackTable.items():
                if video not in self._model.getSketchBoardVideos():
                    #Remove the widget
                    self._trackList.removeItemWidget(widget)

                    #Retrieve the QListWidgetItem for this widget and delete it
                    for item in self._trackList.findItems() :
                        if self._trackList.itemWidget(item) == widget :

                            #Retrieve the row of the item
                            row = self._trackList.row(item)

                            #Delete the element
                            listElement = self._trackList.takeItem(row)
                            del listElement
                            #Update the reference table
                            self._videoTrackTable.pop(widget)


            self._stackedWidget.setCurrentIndex(1)

    # ----------------------- SIGNAL / SLOT ----------------------------------- #
    def addVideo(self):
        """ Retrieve the currently selected video from the session view to add it directly as a track """
        video = self._sessionView.getList().currentItem().data(QtCore.Qt.UserRole)
        self.newTrack(video)

    def suppressVideo(self):
        """ Retrieve the currently selected video from the sktech board view to remove it """
        video = self._trackList.selectedItems()[0]
        self.removeTrack(video)

    # ----------------------- EVENT HANDLERS -------------------------------- #
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("app/video"):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("app/video"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.newTrack(event.mimeData().data("app/video"))

        event.setDropAction(QtCore.Qt.CopyAction)
        event.accept()
