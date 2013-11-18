#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
from PySide import QtGui, QtCore


class Video(object):

    def __init__(self, path):
        super(Video, self).__init__()

        self._path = os.path.abspath(path)
        self._name = None
        self._duration = None
        self._weight = None # in bytes
        self._height = None
        self._width = None
        self._fps = None

        self.extractInformations()
        print str(self)

    def extractInformations(self):
        #Get the size in bytes of the video file
        self._weight = os.path.getsize(self._path)
        self._name = os.path.basename(self._path)

        #Opencv extracting
        capture = cv2.VideoCapture()
        if capture is False:
            raise RuntimeError("The video could not be loaded.")

        #Retrieve the main informations
        self._fps = capture.get(5)
        self._height = capture.get(4)
        self._width = capture.get(3)

    def getListWidget(self):
        """Draw the video under the shape of a list item widget"""
        listWidget = QtGui.QListWidgetItem()

        return listWidget

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