#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from core.Project import Project

class Session():

    def __init__(self):
        super(Session).__init__()

        #Store the projects in the current session
        self._projectsList = []

    def newProject(self, name, path):
        """
        Create a Project.
        :param name : the name of the Project
        :param path: the absolute path of the Project
        :type name: str
        :type path: str
        """

        if not type(name) is str:
            raise TypeError('Non correct Project name : a string is expected.')

        #Test if the path is a valid directory
        elif not os.path.isdir(path):
            raise NotADirectoryError()
        else:
            #Create the project save file
            try:
                f = open(os.path.join(path, str(name)+".ewp"), "w")
            except IOError:
                pass
            project = Project(name, path)
            self._projectsList.append(project)

    def openProject(self, path):
        #TODO
        pass
