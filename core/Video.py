#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import math


class Video(object):

    def __init__(self, path):
        super(Video, self).__init__()

        self._path = os.path.abspath(path)
        self._name = None #Name with the extension
        self._simpleName = None #Name without extension
        self._duration = None
        self._weight = None # in bytes
        self._height = None
        self._width = None
        self._fps = None
        self._thumbnail = None

        self.extractInformations()

    def extractInformations(self):
        #Get the size in bytes of the video file
        self._weight = os.path.getsize(self._path)
        self._name = os.path.basename(self._path)
        self._simpleName = os.path.splitext(self._name)[0]

        #Opencv extracting
        capture = cv2.VideoCapture(self._path)
        if capture is False:
            raise RuntimeError("The video could not be loaded.")

        #Retrieve the main informations
        self._fps = capture.get(5)
        self._height = capture.get(4)
        self._width = capture.get(3)

        capture.release()

        self.extractThumbnail()

    def extractThumbnail(self):
        """ Extract a single frame from around 1/3 of the video. If the video is updated, then the thumbnail is recreated."""

        #Create a capture with the video file
        capture = cv2.VideoCapture(self._path)

        #Move the video to 1/3
        frameCount = capture.get(7)
        capture.set(1, math.floor(frameCount/3))

        #Grab the frame
        value,snapshot = capture.read()
        if value is True :
            save = cv2.imwrite(str("data/"+ self._simpleName +".jpg"), snapshot)
            if not save is True:
                raise Exception("Error while saving a snapshot of the video : " + str(self._name))
        else:
            raise Exception("Couldn't read the video : " + str(self._name))

        #Free the resources, not mandatory with Pyhton
        capture.release()


    # ---------------------- BUILT-IN FUNCTIONS ------------------------- #

    def __str__(self):
        #String representation
        return 'Video => name ' + str(self._name) + '/ VideoPath : ' + str(self._path) + ' / VideoWeight : ' + str(self._weight)

    def __eq__(self, other):
        #Stand for the == compare
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

    # ----------------------------- GETTER / SETTER ---------------------------- #

    def getName(self):
        return self._name

    def getPath(self):
        return self._path

    def getWeight(self):
        return self._weight

    def getDuration(self):
        return self._duration

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getFPS(self):
        return self._fps

    def getThumbnail(self):
        return self._thumbnail