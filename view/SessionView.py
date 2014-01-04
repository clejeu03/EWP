#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.SessionViewItem import SessionViewItem

class SessionView(QtGui.QStackedWidget) :

    def __init__(self, app, session):
        super(SessionView, self).__init__()

        self._app = app
        self._model = session

        #Main elements
        self.list = None
        self.title = None

        #Init the view
        self.init()

    def init(self):
        """ Draw the session view for the first time """

        self.addWidget(self.createEmptyProjectWidget())
        self.addWidget(self.initListWidget())

        #Decide which widget the Session will display
        if self._model.currentProject() is None:
            self.setCurrentIndex(0)
        else:
            self.setCurrentIndex(1)

    def initListWidget(self):
        """
        Init the main widget of the project that is shown when the project contains videos. This widget is composed of a
        title in a QLabel, and a list of video items in a QListWidget.
        :return type: QWidget
        """
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()
        self.title = QtGui.QLabel()
        layout.addWidget(self.title)
        self.list = QtGui.QListWidget()
        layout.addWidget(self.list)
        widget.setLayout(layout)

        return widget

    def createEmptyProjectWidget(self):
        """
        This function creates a widget that is shown only if the current project is empty. This widget tells the user that
        he should create a project.
        :return type: QWidget
        """
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel("There is no project. Please create or open one.")
        layout.addWidget(label)
        widget.setLayout(layout)

        return widget

    def suppressVideo(self):
        """ This function calls the controller function to suppress physically the video from the project directory nd to clean up the project data"""

        #Retrieve the current selected item of the session view.
        video = self.list.currentItem().data(QtCore.Qt.UserRole)
        #TODO : refactoring
        self._app.suppressVideo(video)

    def playVideo(self):
        """ This function forward to the controller a call to play the selected video in a new player window   """
        video = self.list.currentIndex().data(QtCore.Qt.UserRole)
        #TODO : refactoring
        #self._app.playVideo(video)

    def update(self):
        """ Update the view with the model data"""

        #TODO : check if the order of the video in the view is different before and after updating

        #Update the widget shown in the session view
        if self._model.currentProject() is None:
            self.setCurrentIndex(0)
        else:
            #Update the project title if it has changed
            if self._model.currentProject().getName() != self.title.text() :
                self.title.setText(self._model.currentProject().getName())

            #Update the list if it has changed
            if not self.list is None:
                #Clear the view by erasing all the items of the list
                self.list.clear()

                #Create items according to those contained in the Project data
                for video in self._model.currentProject().getVideos():
                    #Prepare the view of each item in the project
                    listItem = QtGui.QListWidgetItem()
                    listItem.setData(QtCore.Qt.UserRole, video)
                    itemWidget = SessionViewItem(video, self)
                    self.list.addItem(listItem)
                    self.list.setItemWidget(listItem, itemWidget)

            #Show this widget
            self.setCurrentIndex(1)

        return list


