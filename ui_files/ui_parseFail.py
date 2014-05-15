# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_parseFail.ui'
#
# Created: Tue Mar 18 13:58:30 2014
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

class Ui_ParseHasFailedDialog(object):
    def setupUi(self, ParseHasFailedDialog):
        ParseHasFailedDialog.setObjectName(_fromUtf8("ParseHasFailedDialog"))
        ParseHasFailedDialog.resize(280, 161)
        self.verticalLayout = QtGui.QVBoxLayout(ParseHasFailedDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 41, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.labelParseFail = QtGui.QLabel(ParseHasFailedDialog)
        self.labelParseFail.setObjectName(_fromUtf8("labelParseFail"))
        self.verticalLayout.addWidget(self.labelParseFail)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonOk = QtGui.QPushButton(ParseHasFailedDialog)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ParseHasFailedDialog)
        QtCore.QMetaObject.connectSlotsByName(ParseHasFailedDialog)

    def retranslateUi(self, ParseHasFailedDialog):
        ParseHasFailedDialog.setWindowTitle(_translate("ParseHasFailedDialog", "Dialog", None))
        self.labelParseFail.setText(_translate("ParseHasFailedDialog", "TextLabel", None))
        self.pushButtonOk.setText(_translate("ParseHasFailedDialog", "OK", None))

import resources_rc
