# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_points.ui'
#
# Created: Tue Jan 07 16:12:13 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_pointsMessage(object):
    def setupUi(self, pointsMessage, points, max):
        pointsMessage.setObjectName(_fromUtf8("pointsMessage"))
        pointsMessage.resize(501, 480)
        self.widget = QtGui.QWidget(pointsMessage)
        self.widget.setGeometry(QtCore.QRect(60, 190, 383, 143))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(381, 0))
        self.label.setMaximumSize(QtCore.QSize(381, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 78, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(188, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(pointsMessage, points, max)
        QtCore.QMetaObject.connectSlotsByName(pointsMessage)

    def retranslateUi(self, pointsMessage, points, max):
        percentageScored = (points / float(max)) * 100
        if percentageScored >= 60:
            self.pushButton_2.setVisible(False)
        pointsMessage.setWindowTitle(_translate("pointsMessage", "Punkte", None))
        self.label.setText(_translate("pointsMessage", "<html><head/><body><p align=\"center\">" + str(percentageScored) + "%"    "<br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("pointsMessage", "Training", None))
        self.pushButton.setText(_translate("pointsMessage", "Ok", None))

import resources_rc
