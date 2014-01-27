# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uberBox.ui'
#
# Created: Fri Jan 24 14:51:10 2014
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

class Ui_uberBox(object):
    def setupUi(self, uberBox):
        uberBox.setObjectName("uberBox")
        uberBox.resize(453, 390)
        self.verticalLayout_2 = QtGui.QVBoxLayout(uberBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(uberBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(uberBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 53, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(uberBox)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_4 = QtGui.QLabel(uberBox)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(uberBox)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_6 = QtGui.QLabel(uberBox)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(uberBox)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_8 = QtGui.QLabel(uberBox)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtGui.QSpacerItem(20, 52, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)

        self.retranslateUi(uberBox)
        QtCore.QMetaObject.connectSlotsByName(uberBox)

    def retranslateUi(self, uberBox):
        uberBox.setWindowTitle(_translate("uberBox", "Über", None))
        self.label.setText(_translate("uberBox", "<html><head/><body><p><img src=\":/df/inst_hsr.gif\"/></p></body></html>", None))
        self.label_2.setText(_translate("uberBox", "<html><head/><body><p><img src=\":/df/logo.png\"/></p></body></html>", None))

import resources_rc
