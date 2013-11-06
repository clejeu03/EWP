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

    def initView(self):
        """ Draw the main docked widget of the mainWindow"""
        self.sessionView = SessionView(self._controller)


    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)