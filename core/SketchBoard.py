#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class SketchBoard(object) :

    def __init__(self):
        super(SketchBoard, self).__init__()

        self._videoList = []

        self._maxVideos = 20
