# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Jan 16 14:50:56 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(585, 630)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem14 = QtGui.QSpacerItem(124, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_2.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_3.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_4.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_5.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_6.setText(_translate("Dialog", "PushButton", None))

import resources_rc
