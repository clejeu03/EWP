#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from view.MainWindow import MainWindow
from core.Session import Session


class Controller(object):

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
        self._session.newProject('Project2', "C:/Users/Cecilia/Documents/")

        print str('recent projects : ' + str(self._session.recentProjects()))
        print str('current projects : ' + str(self._session.currentProjects()))

        self._session.closeProject(self._session.currentProjects()[1])
        print str('Removed...')

        print str('recent projects : ' + str(self._session.recentProjects()))
        print str('current projects : ' + str(self._session.currentProjects()))

        self._session.currentProjects()[0].addVideo('Big_buck_bunny.avi')
        #self._session.currentProjects()[0].addVideo('misfits.avi')

        print str('added video...')

        print str(self._session.currentProjects()[0])

#------------------------------------------------------------------------------------#
    def saveCurrentSession(self):
        #TODO : use pickle module for serilization
        pass

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow


