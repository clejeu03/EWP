#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2


class Video(object):

    def __init__(self, path):
        super(Video, self).__init__()

        self._path = os.path.abspath(path)
        self._name = None
        self._duration = None
        self._weight = None # in bytes
        self._format = None

        self.extractInformations()
        print str(self)

    def extractInformations(self):
        #Get the size in bytes of the video file
        self._weight = os.path.getsize(self._path)
        completeName = os.path.split(self._path)[1]
        self._name = completeName.split(".")[0]
        self._format = completeName.split(".")[1]

        #Opencv extracting
        print 'path : ' + str(self._path)
        capture = cv2.VideoCapture()

        print 'capture : ' + str(capture.open(str('Big_buck_bunny.avi')))
        format = capture.get(8)
        height = capture.get(4)
        width = capture.get(3)

        print 'opencv => format : ' + str(format) + ' / height : ' + str(height) + ' / width : ' + str(width)

    # ---------------------- BUILT-IN FUNCTIONS ------------------------- #

    def __str__(self):
        #String representation
        return 'Video => name ' + str(self._name) + '/ path : ' + str(self._path) + ' / weight : ' + str(self._weight)

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