#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.Session import Session
import os

class Controller(object):

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None
        self._session = None


        self.initSession()

        #Temporary !
        #self.test()
        self.createNewProject()
        #self._session.newProject('Project1', '/home/cecilia/Documents/')
        self._session.currentProject().addVideo('/home/cecilia/Vidéos/Big_buck_bunny.avi')

#------------------------------------------------------------------------------------#
    def test(self):
        #Temporary !
        self._session.newProject('Project1', '/home/cecilia/Documents/')
        self._session.newProject('Project2', '/home/cecilia/Documents/')


        print str('recent projects : ' + str(self._session.recentProjects()))
        print str('current projects : ' + str(self._session.getProjectList()))

        self._session.closeProject(self._session.currentProject())
        print str('Removed...')

        print str('recent projects : ' + str(self._session.recentProjects()))
        print str('current projects : ' + str(self._session.getProjectList()))

        self._session.currentProject().addVideo('/home/cecilia/Vidéos/Big_buck_bunny.avi')
        #self._session.currentProject().addVideo('misfits.avi')

        print str('added video...')

        print str(self._session.currentProject())


#------------------------------------------------------------------------------------#
    def createNewProject(self):
        """ Open a file dialog to create a new directory for the project """

        name = "ProjectPlop"
        path = "/home/cecilia/Documents/"

        #TODO : dialog
        if not type(name) is str:
            raise TypeError('Non correct Project name : a string is expected.')
        #Test if the path is a valid directory
        elif not os.path.isdir(path):
            raise NotADirectoryError()
        else:
            #Create the directory for the project and fill
            projectPath = path + name
            os.mkdir(projectPath)
            os.mkdir(projectPath + os.sep + "Video Files")
            self._session.newProject(name, projectPath)

    def saveCurrentSession(self):
        #TODO : use pickle module for serilization
        pass

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

    def getSession(self):
        return self._session


