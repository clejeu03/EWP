#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):

    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self._controller = controller
        label = QtGui.QLabel('plop')
        label.show()
        self.setWindowTitle('EWP')

