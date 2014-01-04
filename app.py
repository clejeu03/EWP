#!/usr/bin/env python
# -*- coding: utf-8 -*-

class App(object):

    def __init__(self):
        super(App, self).__init__()

        self._mainWindow = None


    # --------------------- GETTER / SETTER ---------------------- #

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

