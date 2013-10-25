#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):

    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self._controller = controller
        self.setWindowTitle('EWP')

        #Restore the users parameters
        settings = QtCore.QSettings("Cecilia", "EWP")
        geometry = settings.value("geometry", self.saveGeometry())
        self.restoreGeometry(geometry)

    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)