#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from kloud_config.ui on Mon Aug  3 01:18:50 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_Kloud(object):
    def setupUi(self, Kloud):
        Kloud.setObjectName("Kloud")
        Kloud.resize(400, 400)
        Kloud.setMinimumSize(QtCore.QSize(379, 279))
        self.verticalLayoutWidget = QtGui.QWidget(Kloud)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.showSecondHandCheckBox = QtGui.QCheckBox(self.groupBox)
        self.showSecondHandCheckBox.setGeometry(QtCore.QRect(0, 30, 370, 23))
        self.showSecondHandCheckBox.setObjectName("showSecondHandCheckBox")
        self.showSecondHandCheckBox_2 = QtGui.QCheckBox(self.groupBox)
        self.showSecondHandCheckBox_2.setGeometry(QtCore.QRect(0, 60, 370, 23))
        self.showSecondHandCheckBox_2.setObjectName("showSecondHandCheckBox_2")
        self.showSecondHandCheckBox_3 = QtGui.QCheckBox(self.groupBox)
        self.showSecondHandCheckBox_3.setGeometry(QtCore.QRect(0, 90, 370, 23))
        self.showSecondHandCheckBox_3.setObjectName("showSecondHandCheckBox_3")
        self.showSecondHandCheckBox_4 = QtGui.QCheckBox(self.groupBox)
        self.showSecondHandCheckBox_4.setGeometry(QtCore.QRect(0, 120, 370, 23))
        self.showSecondHandCheckBox_4.setObjectName("showSecondHandCheckBox_4")
        self.showSecondHandCheckBox_5 = QtGui.QCheckBox(self.groupBox)
        self.showSecondHandCheckBox_5.setGeometry(QtCore.QRect(0, 150, 370, 23))
        self.showSecondHandCheckBox_5.setObjectName("showSecondHandCheckBox_5")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Kloud)
        QtCore.QMetaObject.connectSlotsByName(Kloud)

    def retranslateUi(self, Kloud):
        Kloud.setWindowTitle(kdecore.i18n("Form"))
        self.groupBox.setTitle(kdecore.i18n("Kloud - AWS Plasmoid"))
        self.showSecondHandCheckBox.setToolTip(kdecore.i18n("Show the seconds"))
        self.showSecondHandCheckBox.setWhatsThis(kdecore.i18n("Check this if you want to show the seconds."))
        self.showSecondHandCheckBox.setText(kdecore.i18n("Show Instances"))
        self.showSecondHandCheckBox_2.setToolTip(kdecore.i18n("Show the seconds"))
        self.showSecondHandCheckBox_2.setWhatsThis(kdecore.i18n("Check this if you want to show the seconds."))
        self.showSecondHandCheckBox_2.setText(kdecore.i18n("Show Images"))
        self.showSecondHandCheckBox_3.setToolTip(kdecore.i18n("Show the seconds"))
        self.showSecondHandCheckBox_3.setWhatsThis(kdecore.i18n("Check this if you want to show the seconds."))
        self.showSecondHandCheckBox_3.setText(kdecore.i18n("Show EBS Volumes"))
        self.showSecondHandCheckBox_4.setToolTip(kdecore.i18n("Show the seconds"))
        self.showSecondHandCheckBox_4.setWhatsThis(kdecore.i18n("Check this if you want to show the seconds."))
        self.showSecondHandCheckBox_4.setText(kdecore.i18n("Show Elastic IPs"))
        self.showSecondHandCheckBox_5.setToolTip(kdecore.i18n("Show the seconds"))
        self.showSecondHandCheckBox_5.setWhatsThis(kdecore.i18n("Check this if you want to show the seconds."))
        self.showSecondHandCheckBox_5.setText(kdecore.i18n("Show availability zones"))

