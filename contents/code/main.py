#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
import logging
from logger import logger as log
log.setLevel(logging.DEBUG)
 
class AWSPlasmoid(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
 
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
 
        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        label = Plasma.Label(self.applet)
        label.setText("Hello world!")
        self.layout.addItem(label)
        self.setLayout(self.layout)
        self.resize(125,125)
        self.connectToEngine()
 
    #def paintInterface(self, painter, option, rect):
        #painter.save()
        #painter.setPen(Qt.white)
        #painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "AWS Plasmoid!")
        #painter.restore()
    
    def connectToEngine(self):
        log.debug("connectToEngine")
        self.awsEngine = self.dataEngine("awsengine")
        self.awsEngine.connectSource("images", self, 6000, Plasma.AlignToMinute)

    @pyqtSignature("dataUpdated(const QString &, const Plasma::DataEngine::Data &)")
    def dataUpdated(self, sourceName, data):
        log.debug("dataUpdated")
        self.images = data
        log.debug("self.images = %s" % self.images)
        self.update()
 
def CreateApplet(parent):
    return AWSPlasmoid(parent)
