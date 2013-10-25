#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.Project import Project

class Session():

    def __init__(self):
        super(Session).__init__()

        self._projectsList = []

    def newProject(self, name, path):
        """
        Create a Project.
        :param name : the name of the Project
        :param path: the absolute path of the Project
        :type name: str
        :type path: str
        """
        project = Project(name, path)
        self._projectsList.append(project)
