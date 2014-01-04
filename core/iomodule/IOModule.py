#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class IOModule(object):

    def __init__(self, app):
        super(IOModule, self).__init__()

        self._app = app

    def suppressVideo(self, path):
        """ Suppress the video to the given path  """
        #List all the videos contained into the video files folder of the project directory
        videoList = os.listdir(self._app.getSession().currentProject().getPath() + os.sep + "VideoFiles")

        #When the name matches, then suppress the video file corresponding
        for item in videoList:
            if item == path.getName() :
                os.remove(self._app.getSession().currentProject().getPath() + os.sep + "Video Files" + os.sep + item)
                self._app.getSession().currentProject().suppressVideo(path)

        #Update the view
        self._app.update()
