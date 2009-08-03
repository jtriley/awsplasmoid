#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdecore import *
from PyKDE4.kdeui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from kloud_config import *

import logging
from logger import logger as log
log.setLevel(logging.DEBUG)

class KloudConfig(QWidget,Ui_Kloud):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.connect(self.localTimeZone, SIGNAL("stateChanged(int)"), self, SLOT("slotLocalTimeZoneToggled(int)"))
 
class AWSPlasmoid(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.dialog = None
        self.setHasConfigurationInterface(True)
        self.setAspectRatioMode(Plasma.Square)
 
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
 
        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        label = Plasma.Label(self.applet)
        label.setText("Kloud - AWS Plasmoid ")
        self.layout.addItem(label)
        self.setLayout(self.layout)
        self.resize(125,125)
        self.connectToEngine()

    def showConfigurationInterface(self):
        windowTitle = str(self.applet.name()) + " Settings" #i18nc("@title:window", "%s Settings" % str(self.applet.name()))

        if self.dialog is None:
            self.dialog = KDialog(None)
            self.dialog.setWindowTitle(windowTitle)
            
            self.ui = KloudConfig(self.dialog)
            self.dialog.setMainWidget(self.ui)
            
            self.dialog.setButtons(KDialog.ButtonCodes(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel | KDialog.Apply)))
            self.dialog.showButton(KDialog.Apply, False)
            
            self.connect(self.dialog, SIGNAL("applyClicked()"), self, SLOT("configAccepted()"))
            self.connect(self.dialog, SIGNAL("okClicked()"), self, SLOT("configAccepted()"))

        #self.ui.showTimeStringCheckBox.setChecked(self.showTimeString)
        #self.ui.showSecondHandCheckBox.setChecked(self.showSecondHand)
        #self.ui.localTimeZone.setChecked(self.isLocalTimezone())
        #self.ui.timeZones.setSelected(self.currentTimezone, True)
        #self.ui.timeZones.setEnabled(not self.isLocalTimezone())

        self.dialog.show()

    #def paintInterface(self, painter, option, rect):
        #painter.save()
        #painter.setPen(Qt.white)
        #painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "AWS Plasmoid!")
        #painter.restore()
    
    def connectToEngine(self):
        log.debug("connectToEngine")
        self.awsEngine = self.dataEngine("awsengine")
        self.awsEngine.connectSource("images", self, 6000, Plasma.AlignToMinute)
        self.awsEngine.connectSource("instances", self, 6000, Plasma.AlignToMinute)

    @pyqtSignature("configAccepted(void)")
    def configAccepted(self):
        log.info('Configuration file saved')

    @pyqtSignature("dataUpdated(const QString &, const Plasma::DataEngine::Data &)")
    def dataUpdated(self, sourceName, data):
        log.debug("dataUpdated: %s" % sourceName)
        self.images = data
        log.debug("self.images = %s" % self.images)

        for img in self.images:
            label = Plasma.Label(self.applet)
            label.setText('image')
            self.layout.addItem(label)

        self.update()
 
def CreateApplet(parent):
    return AWSPlasmoid(parent)
