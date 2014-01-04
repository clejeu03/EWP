#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from core.Project import Project


class Session(object):

    def __init__(self):
        super(Session, self).__init__()

        #Store the projects in the current session
        self._projectsList = []

        #Store in a stack FIFO the recent projects
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
        project = Project(name, path)

        self.openProject(project)

    def openProject(self, project):
        """
        Create a Project.
        :param name : the name of the Project
        :param path: the absolute path of the Project
        :type name: str
        :type path: str
        """
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

    def getProjectList(self):
        return self._projectsList

    def currentProject(self):
        """
        CAUTION : this function was valuable as long as there is only one project in a Session
        Retrieve the first project of the list, or the only one if there is only one project at a time
        """
        if len(self._projectsList) != 0:
            return self._projectsList[0]
        else:
            return None

    def getMaxRecentProject(self):
        return self._maxRecentProjects

    def setMaxRecentProjects(self, number):
        self._maxRecentProjects = number
