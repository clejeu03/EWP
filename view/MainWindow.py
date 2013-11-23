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

        self.loadStyleSheet()
        self.initView()

    def loadStyleSheet(self, styleFile=None):
        """
        Retrieve the style describe in a css file into the application
        :param styleFile: the name of the file, supposing it's belong to the resources folder, if there isn't, then the default style is applied
        :type styleFile: string
        """

        #Read the default file
        file = QtCore.QFile("resources/styles/default.css")
        if not file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text) is True :
            raise IOError("Can't load the style file.")
        stylesheet = file.readAll()

        #Conversion from QByteArray to Unicode String
        codec = QtCore.QTextCodec.codecForName("KOI8-R")
        string = codec.toUnicode(stylesheet)

        #Apply the style to the whole application
        self.setStyleSheet(string)

    def initView(self):
        """ Draw the main docked widget of the mainWindow"""

        #Draw the Session View
        self._sessionView = SessionView(self._controller)
        leftDockWidget = QtGui.QDockWidget("Session", self)
        leftDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        leftDockWidget.setWidget(self._sessionView)
        leftDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)

        #temporary !
        titleBar = QtGui.QWidget()
        leftDockWidget.setTitleBarWidget(titleBar)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, leftDockWidget)

        #Draw the central widget
        self.mdiArea = QtGui.QMdiArea()
        self.setCentralWidget(self.mdiArea)

        #Draw the Player View
        rightDockWidget = QtGui.QDockWidget("Player", self)
        rightDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        #rightDockWidget.setWidget(self.player)
        rightDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, rightDockWidget)




    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)

    #------------------------ GETTER / SETTER ------------------------ #

    def getSessionView(self):
        return self._sessionView