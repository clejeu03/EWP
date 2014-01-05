#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SketchWidget (QtGui.QFrame):

    def __init__(self):
        super(SketchWidget, self).__init__()

        self.setMinimumWidth(100)
        self.setMinimumHeight(30)

        #For the style sheet
        self.setObjectName("sketch")
