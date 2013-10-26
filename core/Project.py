#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Project:

    def __init__(self, name, path):
        super(Project, self).__init__()

        self._name = name
        self._path = path

        print('name : ' + str(self._name))
        print('path : ' + str(self._path))

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