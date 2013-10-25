#!/usr/bin/env python
# -*- coding: utf-8 -*-

from view.MainWindow import MainWindow

class Controller():

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow




