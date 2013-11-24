#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.Session import Session
from PySide import QtCore
import shutil
import os

class Controller(object):

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None
        self._session = None


        self.initSession()

        #Temporary !
        #self.createNewProject()
        #self.importVideo()


    def createNewProject(self, name, path):
        """ Create a new Project by choosing a directory for saving it """

        if not type(name) is str:
            raise TypeError('Non correct Project name : a string is expected.')

        #Test if the path is a valid directory
        elif not os.path.isdir(path):
            raise NotADirectoryError()
        else:
            #Create the directory for the project and fill
            projectPath = path + os.sep + name
            os.mkdir(projectPath)
            os.mkdir(projectPath + os.sep + "Video Files")
            self._session.newProject(name, projectPath)
            self._mainWindow.update()

    def importVideo(self):
        """
        Open a dialog for the user to choose a video to import into the current project,
        then copy the video into the project folder and create the Video class corresponding.
        """
        path = "/home/cecilia/Vidéos/Big_buck_bunny.avi"
        name = os.path.basename(path)

        #TODO : dialog

        #Copy the video file
        videoProjectPath = self._session.currentProject().getPath() + os.sep + "Video Files"
        shutil.copy(path, videoProjectPath)

        #Create the video class
        self._session.currentProject().addVideo(videoProjectPath + os.sep + name)

    def suppressVideo(self, video):
        """
        Suppress a video from the project directory and forward the instructions to the current project
        """
        #List all the videos contained into the video files folder of the project directory
        videoList = os.listdir(self._session.currentProject().getPath() + os.sep + "Video Files")

        #When the name matches, then suppress the video file corresponding
        for item in videoList:
            if item == video.getName() :
                os.remove(self._session.currentProject().getPath() + os.sep + "Video Files" + os.sep + item)
                self._session.currentProject().suppressVideo(video)

        #Update the view
        self._mainWindow.update()

    def saveCurrentSession(self):
        #TODO : use pickle module for serilization
        pass

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

    def getSession(self):
        return self._session


