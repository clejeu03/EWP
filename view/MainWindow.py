#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from view.SessionView import SessionView
from view.NewProjectDialog import NewProjectDialog

class MainWindow(QtGui.QMainWindow):

    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self._controller = controller
        self.setWindowTitle('EWP')

        #Actions


        #Main Widgets
        self._sessionView = None

        #Restore the users parameters
        settings = QtCore.QSettings("Cecilia", "EWP")
        geometry = settings.value("geometry", self.saveGeometry())
        self.restoreGeometry(geometry)

        self.loadStyleSheet()
        self.createAction()
        self.initMenu()
        self.initView()

    def loadStyleSheet(self, styleFile=None):
        """
        Retrieve the style describe in a css file into the application
        :param styleFile: the name of the file, supposing it's belong to the resources folder, if there isn't, then the default style is applied
        :type styleFile: string
        """

        #Read the default file
        file = QtCore.QFile("resources/styles/default.css")
        if not file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text) is True :
            raise IOError("Can't load the style file.")
        stylesheet = file.readAll()

        #Conversion from QByteArray to Unicode String
        codec = QtCore.QTextCodec.codecForName("KOI8-R")
        string = codec.toUnicode(stylesheet)

        #Apply the style to the whole application
        self.setStyleSheet(string)

    def initView(self):
        """ Draw the main docked widget of the mainWindow"""

        #Draw the Session View
        self._sessionView = SessionView(self._controller)
        leftDockWidget = QtGui.QDockWidget("Session", self)
        leftDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        leftDockWidget.setWidget(self._sessionView)
        leftDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)

        #temporary !
        titleBar = QtGui.QWidget()
        leftDockWidget.setTitleBarWidget(titleBar)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, leftDockWidget)

        #Draw the central widget
        self.mdiArea = QtGui.QMdiArea()
        self.setCentralWidget(self.mdiArea)

        #Draw the Player View
        rightDockWidget = QtGui.QDockWidget("Player", self)
        rightDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        #rightDockWidget.setWidget(self.player)
        rightDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, rightDockWidget)


    def initMenu(self):
        """
        Create the main menu.
        """
        self.fileMenu = self.menuBar().addMenu(self.tr("&File"))
        self.fileMenu.addAction(self.createProjectAction)
        self.fileMenu.addAction(self.openProjectAction)
        self.fileMenu.addAction(self.saveProjectAction)

        self.helpMenu = self.menuBar().addMenu(self.tr("&Help"))
        self.helpMenu.addAction(self.aboutAction)

    def createAction(self):
        """
        Set up all the actions usefull in the main window
        """
        self.createProjectAction = QtGui.QAction(self.tr("&New Project"), self)
        self.createProjectAction.setShortcut(QtGui.QKeySequence.New)
        self.setStatusTip(self.tr("Create a new project"))
        self.connect(self.createProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("newProject()"))

        self.openProjectAction = QtGui.QAction(self.tr("&Open..."), self)
        self.openProjectAction.setShortcut(QtGui.QKeySequence.Open)
        self.setStatusTip(self.tr("Open an existing project"))
        self.connect(self.openProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("openProject()"))

        self.saveProjectAction = QtGui.QAction(self.tr("&Save"), self)
        self.saveProjectAction.setShortcut(QtGui.QKeySequence.Save)
        self.setStatusTip(self.tr("Save the current project"))
        self.connect(self.saveProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("save()"))

        self.aboutAction = QtGui.QAction(self.tr("&About"), self)
        self.setStatusTip(self.tr("Show the credits and authors"))
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("showAbout()"))


    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)

    # ------------------------ SIGNAL / SLOTS HANDLER ---------------- #

    def newProject(self):
        """ Forward the creation of a new project to the controller. """

        dialog = NewProjectDialog()

    def openProject(self):
        """ Forward the importation of a new project to the controller. """
        #TODO
        pass

    def showAbout(self):
        """ Show a popup window with authors and credits """
        #TODO
        pass

    def save(self):
        """ Save the current project in its state """
        #TODO
        pass


    #------------------------ GETTER / SETTER ------------------------ #

    def getSessionView(self):
        return self._sessionView