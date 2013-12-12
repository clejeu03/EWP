#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.Session import Session
from view.Player import Player
from view.SketchBoardView import SketchBoardView
from core.SketchBoard import SketchBoard
import pickle
import shutil
import os

class Controller(object):

    def __init__(self):
        super(Controller, self).__init__()

        self._mainWindow = None
        self._session = None
        self._sketchBoard = None
        self.player = Player()

        self.initSession()


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
            os.mkdir(projectPath + os.sep + "VideoFiles")

            #Create the project save file
            try:
                open(os.path.join(projectPath + os.sep + str(name) +".ewp"), "w")
            except IOError:
                pass

            self._session.newProject(name, projectPath)

            #Prepare the timeline view and display it to the main window
            self._sketchBoard = SketchBoard()
            sketchBoardView = SketchBoardView()
            self._mainWindow.setSketchBoardView(sketchBoardView)

            self._mainWindow.update()

    def importVideo(self, path):
        """
        Open a dialog for the user to choose a video to import into the current project,
        then copy the video into the project folder and create the Video class corresponding.
        :param path: the path of the video to be imported in the current project
        :type path: string
        """
        name = os.path.basename(path)

        #Copy the video file
        videoProjectPath = self._session.currentProject().getPath() + os.sep + "VideoFiles"
        shutil.copy(path, videoProjectPath)

        #Create the video class
        self._session.currentProject().addVideo(videoProjectPath + os.sep + name)

        #Update the view
        self._mainWindow.update()

    def suppressVideo(self, video):
        """
        Suppress a video from the project directory and forward the instructions to the current project
        """
        #List all the videos contained into the video files folder of the project directory
        videoList = os.listdir(self._session.currentProject().getPath() + os.sep + "VideoFiles")

        #When the name matches, then suppress the video file corresponding
        for item in videoList:
            if item == video.getName() :
                os.remove(self._session.currentProject().getPath() + os.sep + "Video Files" + os.sep + item)
                self._session.currentProject().suppressVideo(video)

        #Update the view
        self._mainWindow.update()

    def saveCurrentSession(self):
        """ Serialization of the core module using pickle """
        name = self._session.currentProject().getName()
        path = self._session.currentProject().getPath() + os.sep + str(name) + ".ewp"
        print "Save : " + str(self._session.currentProject())
        pickle.dump(self._session.currentProject(), open(path, "wb"))

    def loadSavedFile(self, path):
        """
        Load the file at the given path using pickle module to recreate the classes
        :param path: the path of the save file
        :type path : string
        """
        result = pickle.load(open(path, "rb"))
        print "load : " + str(result)

        self._session.openProject(result)

        self._mainWindow.update()

    def playVideo(self, video):
        """ Open the video in a new window to play it  """

        self.player.start(video)

    def initSession(self):
        self._session = Session()

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

    def getSession(self):
        return self._session


