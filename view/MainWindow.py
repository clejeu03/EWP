#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

from view.SessionView import SessionView
from view.dialogs.NewProjectDialog import NewProjectDialog
from view.sketchViewModule.SketchBoardView import SketchBoardView

class MainWindow(QtGui.QMainWindow):

    def __init__(self, app):
        super(MainWindow, self).__init__()

        self._app = app
        self.setWindowTitle('EWP')

        #Actions


        #Main Widgets
        self._sessionView = None
        self._sketchBoardView = None

        #Restore the users parameters
        settings = QtCore.QSettings("Cecilia", "EWP")
        geometry = settings.value("geometry", self.saveGeometry())
        self.restoreGeometry(geometry)

        self.loadStyleSheet()
        self.createAction()
        self.initMenu()
        self.initStatusBar()
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
        self._sessionView = SessionView(self._app)
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
        #rightDockWidget = QtGui.QDockWidget("Player", self)
        #rightDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        ##rightDockWidget.setWidget(self.player)
        #rightDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        #self.addDockWidget(QtCore.Qt.RightDockWidgetArea, rightDockWidget)

    def initStatusBar(self):
        """ Initialize the status bar of the main window """
        self.statusBar().showMessage(self.tr("Ready"))

    def initMenu(self):
        """
        Create the main menu.
        """
        self.fileMenu = self.menuBar().addMenu(self.tr("&File"))
        self.fileMenu.addAction(self.createProjectAction)
        self.fileMenu.addAction(self.openProjectAction)

        #TODO : problem displaying submenu
        #self.recentMenu = self.fileMenu.addMenu(self.tr("Open &recent"))
        #for recentProject in self._controller.getSession().recentProjects():
            #recentAction = QtGui.QAction(self.tr(str(recentProject.getPath())), self)
            #self.connect(recentAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("openRecent(recentProject.getPath())"))
            #self.recentMenu.addAction(recentAction)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.importVideoAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveProjectAction)

        self.helpMenu = self.menuBar().addMenu(self.tr("&Help"))
        self.helpMenu.addAction(self.aboutAction)

    def createAction(self):
        """
        Set up all the actions usefull in the main window
        """
        self.createProjectAction = QtGui.QAction(self.tr("&New Project"), self)
        self.createProjectAction.setShortcut(QtGui.QKeySequence.New)
        self.createProjectAction.setStatusTip(self.tr("Create a new project"))
        self.connect(self.createProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("newProject()"))

        self.openProjectAction = QtGui.QAction(self.tr("&Open..."), self)
        self.openProjectAction.setShortcut(QtGui.QKeySequence.Open)
        self.openProjectAction.setStatusTip(self.tr("Open an existing project"))
        self.connect(self.openProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("openProject()"))

        self.saveProjectAction = QtGui.QAction(self.tr("&Save"), self)
        self.saveProjectAction.setShortcut(QtGui.QKeySequence.Save)
        self.saveProjectAction.setStatusTip(self.tr("Save the current project"))
        self.connect(self.saveProjectAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("save()"))

        self.importVideoAction = QtGui.QAction(self.tr("&Import video..."), self)
        self.importVideoAction.setStatusTip(self.tr("Import a video into your project"))
        self.connect(self.importVideoAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("importVideo()"))

        self.aboutAction = QtGui.QAction(self.tr("&About"), self)
        self.aboutAction.setStatusTip(self.tr("Show the credits and authors"))
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("showAbout()"))

    # ------------------------- EVENT HANDLERS ------------------------ #
    def closeEvent(self, event):
        """Before really closing, store the preferences of the user and change the _aboutToClose value."""
        settings = QtCore.QSettings("Cecilia", "EWP")
        settings.setValue("geometry", self.saveGeometry())
        super(MainWindow, self).closeEvent(event)

    # ------------------------ SIGNAL / SLOTS HANDLER ---------------- #
    def initSketchBoard(self):
        self._sketchBoardView = SketchBoardView(self._app, self._sessionView)
        bottomDockWidget = QtGui.QDockWidget(self.tr("SketchBoard"), self)
        bottomDockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea | QtCore.Qt.TopDockWidgetArea)
        bottomDockWidget.setWidget(self._sketchBoardView)
        bottomDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetClosable)
        self.setCorner(QtCore.Qt.BottomLeftCorner, QtCore.Qt.LeftDockWidgetArea)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, bottomDockWidget)

    def newProject(self):
        """ Forward the creation of a new project to the application. """
        dialog = NewProjectDialog()
        if not dialog.name is None and not dialog.path is None:
            self._app.createProject(str(dialog.name), str(dialog.path))

    def openProject(self):
        """ Forward the importation of a new project to the application. """
        path, filter = QtGui.QFileDialog.getOpenFileNames(self, str(self.tr("Open a project")), "/home/cecilia/", self.tr("EWP project (*.ewp)"))
        savedPath = path[0].encode("utf-8")
        self._app.loadSavedFile(savedPath)

    def showAbout(self):
        """ Show a popup window with authors and credits """
        about = QtGui.QWidget()

        layout = QtGui.QVBoxLayout()

        labelTitle = QtGui.QLabel("Electronic Wallpaper 2.0")
        layout.addWidget(labelTitle)

        labelDescription = QtGui.QLabel("This software is designed to create new video editing experience. Etc...")
        layout.addWidget(labelDescription)

        labelContact = QtGui.QLabel("For any question please contact : cecilia.lejeu@gmail.com")
        layout.addWidget(labelContact)

        layout.setStretchFactor(labelTitle, 3)
        layout.setStretchFactor(labelDescription, 1)
        layout.setStretchFactor(labelContact, 3)

        about.setLayout(layout)
        about.show()

    def save(self):
        """ Save the current project in its state """
        self._app.save()

    def importVideo(self):
        """ Open a QWizard to help the user choose and import a video  """
        path, filter = QtGui.QFileDialog.getOpenFileNames(self, str(self.tr("Import a video")), "/home/cecilia/", self.tr("Video files (*.avi *.mov)"))
        videoPath = path[0].encode("utf-8")
        self._app.importVideo(videoPath)

    def update(self):
        self._sessionView.update()
        if not self._sketchBoardView is None:
            self._sketchBoardView.update()

    #------------------------ GETTER / SETTER ------------------------ #
    def getSessionView(self):
        return self._sessionView

    def getSketchBoardView(self):
        return self._sketchBoardView
