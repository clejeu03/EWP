#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui

from controller.Controller import Controller
from view.MainWindow import MainWindow

#------------- MAIN --------------#
app = QtGui.QApplication(sys.argv)


#Creation of the main Controller
controller = Controller()

#Creation of the Main Window
mainWindow = MainWindow(controller)
controller.setMainWindow(mainWindow)

#Temporary !
controller.loadSavedFile("/home/cecilia/Documents/ProjectTest/ProjectTest.ewp")

if mainWindow :
    mainWindow.show()

sys.exit(app.exec_())

