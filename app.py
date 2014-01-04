#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.sessionManager.Session import Session
from core.iomodule.IOModule import IOModule

class App(object):

    def __init__(self):
        super(App, self).__init__()

        self._mainWindow = None

        #Components
        self._session = None
        self._iomodule = None

        self.init()

    def init(self):
        """ This function initialize all the components of the app class  """
        self._session = Session()
        self._iomodule = IOModule()

    # --------------------- GETTER / SETTER ---------------------- #

    def getSession(self):
        return self._session

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

