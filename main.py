#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui

from app import App
from view.MainWindow import MainWindow

#------------- MAIN --------------#
#Init Qt
qApp = QtGui.QApplication(sys.argv)

#Initialization of app and main window
app = App()
mainWindow = MainWindow(app)
app.setMainWindow(mainWindow)

#controller.loadSavedFile("/home/cecilia/Documents/ProjectTest/ProjectTest.ewp")

#Show the main window
if mainWindow :
    mainWindow.show()

#Execute qt
sys.exit(qApp.exec_())

