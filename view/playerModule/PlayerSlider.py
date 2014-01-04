#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore


class PlayerSlider(QtGui.QSlider):
    """
    Custom slider for the use of the player. The additional features comparing to a standard slider are the mouse over signal that show
    the time in a sort of tooltip, and the simple click on the slider that changes the current value of the slider.
    """

    def __init__(self, parent=None):
        super(PlayerSlider, self).__init__()

        self.parent = parent
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setMouseTracking(True)

        newValue = QtCore.Signal(int)

        self.initTimeTip()

    def initTimeTip(self):
        """ Show the time in mouse over case, upon the slider  """
        self.timeTip = QtGui.QWidget(self)
        self.timeTip.setWindowFlags(QtCore.Qt.ToolTip)

        layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel()
        layout.addWidget(self.label)

        self.timeTip.setLayout(layout)

    def toTime(self, value):
        """
        Take the value given, normaly connected to the slider value, and transform it into seconds to compute the actual video time position
        :param value : the position of the slider = the number of seconds the video have been played for
        :type value: int
        """
        origin = QtCore.QTime(0, 0, 0)

        #updating the current time following the given value
        currentTime = origin.addSecs(value)

        #Adapting the display to the duration
        if self.parent.video.getDuration() < 3600: #seconds
             return currentTime.toString("mm:ss")
        else:
           return currentTime.toString()


    #------------------------- EVENT HANDLERS ---------------------------- #
    def enterEvent(self, event):
        """ the mouse over the slider make a tooltip appear with the pointed time written """
        newVal = self.minimum() + ((self.maximum()-self.minimum()) * QtGui.QCursor.pos().x()) / self.width()

        if self.timeTip.isVisible() is False:
            self.label.setText(self.toTime(newVal))
            self.timeTip.move(QtGui.QCursor.pos().x(),  self.mapToParent(QtCore.QPoint(self.rect().x(), self.rect().y())).y() + 2.5*self.rect().height())
            self.timeTip.show()

    def mouseMoveEvent(self, event):
        """ Override the mouse move function, update the tooltip showing the time if it exists """
        newVal =  self.minimum() + ((self.maximum()-self.minimum()) * QtGui.QCursor.pos().x()) / self.width()

        if self.timeTip.isVisible() is True:
            self.label.setText(self.toTime(newVal))
            self.timeTip.move(QtGui.QCursor.pos().x(), self.mapToParent(QtCore.QPoint(self.rect().x(), self.rect().y())).y() + 2.5*self.rect().height())

    def leaveEvent(self, event):
        """ hide the tooltip """
        if self.timeTip.isVisible() is True:
            self.timeTip.hide()

    def mousePressEvent(self, event):
        """
        The simple left click on the slider must update the value of the slider
        CAUTION : because of the detection of handle click, it's now impossible to drag the slider
        """

        #Retrieve the cursor shape to not consider click on it
        opt = QtGui.QStyleOptionSlider()
        self.initStyleOption(opt)
        handleRect = self.style().subControlRect(QtGui.QStyle.CC_Slider, opt, QtGui.QStyle.SC_SliderHandle, self)

        #Consider only left click event , and not on the handle
        if event.button() == QtCore.Qt.LeftButton and handleRect.contains(event.pos()) is False:

            newVal = self.minimum() + ((self.maximum()-self.minimum()) * event.x()) / self.width()
            if self.invertedAppearance():
                self.setValue( self.maximum() - newVal )
                self.newValue.emit(newVal)
            else:
                self.setValue(newVal)
                self.newValue.emit(newVal)


