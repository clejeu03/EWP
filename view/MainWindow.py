#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.SessionView import SessionView

class MainWindow(QtGui.QMainWindow):

    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self._controller = controller
        self.setWindowTitle('EWP')

        #Main Widgets
        self._sessionView = None

        #Restore the users parameters
        settings = QtCore.QSettings("Cecilia", "EWP")
        geometry = settings.value("geometry", self.saveGeometry())
        self.restoreGeometry(geometry)

        self.initView()

    def initView(self):
        """ Draw the main docked widget of the mainWindow"""

        #Draw the Session View
        self.sessionView = SessionView(self._controller)
        leftDockWidget = QtGui.QDockWidget("", self)
        leftDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        leftDockWidget.setWidget(self.sessionView)
        leftDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, leftDockWidget)

        #Draw the central widget
        self.mdiArea = QtGui.QMdiArea()
        self.setCentralWidget(self.mdiArea)

        #Draw the Player View
        rightDockWidget = QtGui.QDockWidget("", self)
        rightDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        #rightDockWidget.setWidget(self.player)
        rightDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, rightDockWidget)




    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)