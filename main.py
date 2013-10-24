#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore

window = QtGui.QApplication(sys.argv)

label = QtGui.QLabel('Plop')
label.show()

window.exec_()