#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import os

class NewProjectDialog(QtGui.QDialog):

    def __init__(self):
        super(NewProjectDialog, self).__init__()

        self.setModal(True)
        self.setMinimumSize(QtCore.QSize(500, 250))
        self.setWindowTitle(self.tr("Project Creation Dialog"))

        #Field final values
        self.name = None
        self.path = None

        #Elements
        self.label = None
        self.layout = None
        self.nameInput = None
        self.directoryInput = None
        self.directoryErrorMessage = None
        self.cancelButton = None
        self.okButton = None

        #Control
        self.nameCorrect = False
        self.directoryCorrect = False

        self.initView()

    def initView(self):
        """ Set up the main layout of the dialog """

        #TODO : change to grid layout

        self.layout = QtGui.QVBoxLayout()

        #The dialog description
        self.label = QtGui.QLabel("Create a new project.")
        self.layout.addWidget(self.label)

        #The name input label
        nameLayout = QtGui.QHBoxLayout()
        nameLabel = QtGui.QLabel(self.tr("Project Name : "))
        nameLayout.addWidget(nameLabel)
        self.layout.addSpacing(30)

        #The name input
        self.nameInput = QtGui.QLineEdit()
        self.nameInput.setFocus()
        self.nameInput.setMaxLength(20)

        rx = QtCore.QRegExp("\w*")
        validator = QtGui.QRegExpValidator(rx, self)
        self.nameInput.setValidator(validator)

        self.nameInput.setStatusTip(self.tr("Enter a name for the new project"))
        self.nameInput.textChanged.connect(self.nameInputChanged)
        nameLayout.addWidget(self.nameInput)
        self.layout.addLayout(nameLayout)

        #The directory input label
        directoryLayout = QtGui.QHBoxLayout()
        directoryLabel = QtGui.QLabel(self.tr("Location : "))
        directoryLayout.addWidget(directoryLabel)

        #Directory Input
        self.directoryInput = QtGui.QLineEdit()
        self.directoryInput.setStatusTip(self.tr("Choose a directory for the new project"))
        self.directoryInput.textChanged.connect(self.directoryInputChanged)
        directoryLayout.addWidget(self.directoryInput)

        #Browse the existing directories
        directoryBrowseButton = QtGui.QPushButton("...")
        self.connect(directoryBrowseButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("browse()"))
        directoryLayout.addWidget(directoryBrowseButton)
        self.layout.addLayout(directoryLayout)

        #Diretory Error Message
        self.directoryErrorMessage = QtGui.QLabel()
        self.directoryErrorMessage.font().setItalic(True)
        self.layout.addWidget(self.directoryErrorMessage)

        #Buttons
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addSpacing(200)

        #Cancel Button
        self.cancelButton = QtGui.QPushButton(self.tr("Cancel"))
        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))
        buttonsLayout.addWidget(self.cancelButton)

        #OK button
        self.okButton = QtGui.QPushButton(self.tr("OK"))
        self.okButton.setDisabled(True)
        self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("accept()"))

        buttonsLayout.addWidget(self.okButton)
        self.layout.addLayout(buttonsLayout)

        self.setLayout(self.layout)

        #Gather informations at the execution
        if (self.exec_() == QtGui.QDialog.Accepted):
            self.name = self.nameInput.text()
            self.path = self.directoryInput.text()

    @QtCore.Slot(str)
    def nameInputChanged(self, text):
        """
        Control the validity of the name input and enable the ok button according to that result.
        """
        #Check if the name is not an empty string
        if str(self.nameInput.text()) == "":
            print 'empty text ! '
            self.nameCorrect = False
        else:
            #Check if the name is a valid filename
            if self.nameInput.hasAcceptableInput() is True:
                self.nameCorrect = True
            else:
                self.nameCorrect = False

        self.allowOkButton()

    @QtCore.Slot(str)
    def directoryInputChanged(self):
        """
        Control the validity of the directory input and enable the ok button according to that result.
        """
        #Test if the text is valid as a path
        if os.path.exists(str(self.directoryInput.text())) is True:
            self.directoryCorrect = True
            self.directoryErrorMessage.setText("")
        else:
            self.directoryErrorMessage.setText("The location you entered is not valid.")
            self.directoryCorrect = False

        self.allowOkButton()

    def allowOkButton(self):
        """ Manage the enable and disable value of the Ok button according to the value of the field in the dialog """

        if self.nameCorrect is True and self.directoryCorrect is True:
            self.okButton.setDisabled(False)
        else:
            self.okButton.setDisabled(True)

    def browse(self):
        """ Open a file dialog to browse the existing directories and report the name of the selected one in the correct input """

        fileBrowser = QtGui.QFileDialog.getExistingDirectory(self, str(self.tr("Choose a folder")), "/home/cecilia/")
        self.directoryInput.setText(str(fileBrowser))