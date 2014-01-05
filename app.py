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
        self._iomodule = IOModule(self)

    def createProject(self, name, path):
        """ Create a new project by forwarding the creation of folder to IOModule and the creation of the model to the core session manager  """
        projectPath = self._iomodule.createNewProjectDir(name, path)
        self._session.newProject(name, projectPath)
        self._mainWindow.initSketchBoard()
        self.update()

    def importVideo(self, path):
        self._iomodule.importVideo(path)

    def loadSavedFile(self, path):
        value = self._iomodule.loadProject(path)
        self._mainWindow.initSketchBoard()
        self.update()

    def suppressVideo(self, video):
        self._iomodule.suppressVideo(video)

    def save(self):
        self._iomodule.saveCurrent()

    def update(self):
        """ When a changes happened in the core model, then the view need to be updated. That's the purpose of this function.  """
        self._mainWindow.update()

    # --------------------- GETTER / SETTER ---------------------- #

    def getSession(self):
        return self._session

    def setMainWindow(self, mainWindow):
        self._mainWindow = mainWindow

    def getIOModule(self):
        return self._iomodule


