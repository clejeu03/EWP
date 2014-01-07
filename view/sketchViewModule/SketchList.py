#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SketchList(QtGui.QListWidget):

    def __init__(self):
        super(SketchList, self).__init__()

        #For the style sheet
        self.setObjectName("track")

