#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from core.Project import Project


class Session(object):

    def __init__(self):
        super(Session, self).__init__()

        #Store the projects in the current session
        self._projectsList = []
        #Store in a stack LIFO the recent projects
        self._recentProjects = []
        self._maxRecentProjects = 5

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
            project = Project(name, path)
            #Check if the project already exists
            if project in self._projectsList:
                raise Exception('New Project : a project with the same name and location already exists.')
            else:
                #Create the project save file
                try:
                    open(os.path.join(path, str(name)+".ewp"), "w")
                except IOError:
                    pass
                self._projectsList.append(project)
                self.addToRecentProjects(project)

    def addToRecentProjects(self, project):
        """
        Update the list of the recent projects ( 5 projects max)
        :param project: the Project class to be added
        """
        if len(self._recentProjects) == self._maxRecentProjects:
            self._recentProjects.pop()
        self._recentProjects.append(project)

    def addProjectFile(self, path):
        #TODO
        pass

    def closeProject(self, project):
        """
        Close a project and suppress it from the current projects list.
        :param name: the Project class to be closed
        """
        for item in self._projectsList:
            if item == project:
                self._projectsList.remove(project)

    # ---------------------- GETTER / SETTER ------------------------- #

    def recentProjects(self):
        return self._recentProjects

    def currentProjects(self):
        return self._projectsList

    def getMaxRecentProject(self):
        return self._maxRecentProjects

    def setMaxRecentProjects(self, number):
        self._maxRecentProjects = number
