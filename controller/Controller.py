#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from view.MainWindow import MainWindow
from core.Session import Session

class Controller():

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None
        self._session = None

        self.initSession()

        #Temporary !
        self.test()

#------------------------------------------------------------------------------------#
    def test(self):
        #Temporary !
        self._session.newProject('Project1', "C:/Users/Cecilia/Documents/")

#------------------------------------------------------------------------------------#
    def saveCurrentSession(self):
        #TODO : use pickle module for serilization
        pass

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow


