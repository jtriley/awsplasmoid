#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
import logging
from logger import logger
logger.setLevel(logging.DEBUG)
 
class AWSPlasmoid(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.setHasConfigurationInterface(False)
        self.resize(125, 125)
        self.setAspectRatioMode(Plasma.Square)
        self.images = None
        self.connectToEngine()
 
    def paintInterface(self, painter, option, rect):
        painter.save()
        painter.setPen(Qt.white)
        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "AWS Plasmoid!")
        painter.restore()
    
    def connectToEngine(self):
        logger.debug("connectToEngine")
        self.awsEngine = self.dataEngine("awsengine")
        self.awsEngine.connectSource("images", self, 6000, Plasma.AlignToMinute)

    @pyqtSignature("dataUpdated(const QString &, const Plasma::DataEngine::Data &)")
    def dataUpdated(self, sourceName, data):
        logger.debug("dataUpdated")
        self.images = data
        logger.debug("self.images = %s" % self.images)
        self.update()
 
def CreateApplet(parent):
    return AWSPlasmoid(parent)
