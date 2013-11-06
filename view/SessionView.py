#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SessionView(QtGui.QWidget) :

    def __init__(self, controller):
        super(SessionView, self).__init__()

        self.controller = controller


    def update(self):
        """ Update the view with the model data"""
        pass


