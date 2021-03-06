#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.sessionManager.Video import Video

class Project(object):

    def __init__(self, name, path):
        super(Project, self).__init__()

        self._name = name
        self._path = path
        self._videos = []
        self._sketchBoardVideos = [] #/!\ Unique variables : means can't add twice the same video on the sketch board
        #TODO : the possibility of adding multiple times the same video to the sketch board

    def addVideo(self, path):
        """
        Create a Video class from the given file and add the video to the project.
        :param path: the absolute path to the video
        """
        if len(self._videos) < 20 :
            video = Video(path)
            self._videos.append(video)
        else :
            #TODO : message saying that it's the last video that can be added
            pass

    def suppressVideo(self, video):
        """
        Suppress a video from the current project
        """
        if isinstance(video, Video):
            for item in self._videos:
                print "item : " + str(type(item)) + "video : " + str(type(video))
                if item == video:
                    self._videos.remove(video)
                    #If the video is on the sketchboard too, remove it
                    if video in self._sketchBoardVideos:
                        self._sketchBoardVideos.remove(video)
        else:
            raise TypeError("Trying to suppress an item which is not of type Video")

    def newSketchBoardVideo(self, video):
        """ A video need to be added to the sketchboard view, so this function update the model first of all. """

        if video in self._videos:
            self._sketchBoardVideos.append(video)
        else:
            raise Exception("Error : video not recognized.")

    def removeSketchBoardVideo(self, video):
        """ A video need to be removed from the sketch board view, so this function remove it from the model first to update the view after. """
        if video in self._sketchBoardVideos:
            self._sketchBoardVideos.remove(video)
        else :
            raise Exception("Can't find the video")

    # ---------------------- BUILT-IN FUNCTIONS ------------------------- #

    def __str__(self):
        #String representation of the class
        describe = 'Project => name : ' + str(self._name) + ' / path : ' + str(self._path) + ' / videos : ' + str(len(self._videos))
        video = str(self._videos[0])
        sketchBoardVideo = str(self._sketchBoardVideos[0])
        return describe + video + sketchBoardVideo

    def __eq__(self, other):
        #Stands for the == compare
        if self._name == other.getName() and  self._path == other.getPath():
            return True
        else :
            return False

    def __ne__(self, other):
        #Stands for the != compare
        if self._name != other.getName() or self._path != other.getPath():
            return True
        else :
            return False

    # ---------------------- GETTER / SETTER ------------------------- #

    def getName(self):
        return self._name

    def getPath(self):
        return self._path

    def getVideos(self):
        return self._videos

    def getSketchBoardVideos(self):
        return self._sketchBoardVideos