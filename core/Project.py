#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Project:

    def __init__(self, name, path):
        super(Project, self).__init__()

        self._name = name
        self._path = path

        print('name : ' + str(self._name))
        print('path : ' + str(self._path))

