#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import pickle

class IOModule(object):

    def __init__(self, app):
        super(IOModule, self).__init__()

        self._app = app

    def suppressVideo(self, video):
        """
        Suppress the video to the given path
        :param video: the video class that stands for the video file to be removed
        :type video: video
        """
        #List all the videos contained into the video files folder of the project directory
        videoList = os.listdir(self._app.getSession().currentProject().getPath() + os.sep + "VideoFiles")

        #When the name matches, then suppress the video file corresponding
        for item in videoList:
            if item == video.getName() :
                os.remove(self._app.getSession().currentProject().getPath() + os.sep + "Video Files" + os.sep + item)
                self._app.getSession().currentProject().suppressVideo(video)

        #Update the view
        self._app.update()

    def createNewProjectDir(self, name, path):
        """
        Prepare folder for a new project and file to save the project.
        :param name: the project name
        :type name: string
        :param path: the location where the project will be created
        :type path: string
        :return projectPath : the complete name of the .ewp file of the project
        :return type: string
        """

        if not type(name) is str:
            raise TypeError('Non correct Project name : a string is expected.')

        #Test if the path is a valid directory
        elif not os.path.isdir(path):
            raise Exception("Not a directory.")
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

        return projectPath

    def loadProject(self, path):
        """
        Load the file at the given path using pickle module to recreate the classes
        :param path: the path of the save file
        :type path : string
        """
        result = pickle.load(open(path, "rb"))
        self._app.getSession().openProject(result)


    def saveCurrent(self):
        """
        Serialization of the core module using pickle. The data saved are :
        - the class Project that is the current one
        - the class SketchBoardView for the list of the videos in the timeline and the specifications of visualization
        """
        #Retrieve the path of the saved file
        path = self._app.getSession().currentProject().getPath() + os.sep + str(name) + ".ewp"

        #Make up all the data together
        data = []
        data.append(self._app.getSession().currentProject())
        data.append(self._app.)

        #Serialize
        pickle.dump(data, open(path, "wb"), pickle.HIGHEST_PROTOCOL)



    def importVideo(self, path):
        """
        Open a dialog for the user to choose a video to import into the current project,
        then copy the video into the project folder and create the Video class corresponding.
        :param path: the path of the video to be imported in the current project
        :type path: string
        """
        name = os.path.basename(path)

        #Copy the video file
        videoProjectPath = self._app.getSession().currentProject().getPath() + os.sep + "VideoFiles"
        shutil.copy(path, videoProjectPath)

        #Create the video class
        self._app.getSession().currentProject().addVideo(videoProjectPath + os.sep + name)

        #Update the view
        self._app.update()

