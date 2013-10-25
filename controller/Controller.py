#!/usr/bin/env python
# -*- coding: utf-8 -*-

from view.MainWindow import MainWindow
from core.Session import Session

class Controller():

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None
        self._session = None

        self.initSession()

    def saveCurrentSession(self):
        pass

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow
