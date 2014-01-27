# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trainingQuiz.ui'
#
# Created: Thu Jan 16 08:58:14 2014
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

class Ui_trainingQuiz(object):
    def setupUi(self, trainingQuiz):
        trainingQuiz.setObjectName(_fromUtf8("trainingQuiz"))
        trainingQuiz.resize(541, 605)
        trainingQuiz.setAutoFillBackground(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(trainingQuiz)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(17, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(trainingQuiz)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(trainingQuiz)
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(trainingQuiz)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(trainingQuiz)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(trainingQuiz)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_8 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_6 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pushButton_7 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(trainingQuiz)
        QtCore.QMetaObject.connectSlotsByName(trainingQuiz)

    def retranslateUi(self, trainingQuiz):
        trainingQuiz.setWindowTitle(_translate("trainingQuiz", "Training", None))
        self.label.setText(_translate("trainingQuiz", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton.setText(_translate("trainingQuiz", "PushButton", None))
        self.pushButton_2.setText(_translate("trainingQuiz", "PushButton", None))
        self.pushButton_3.setText(_translate("trainingQuiz", "PushButton", None))
        self.pushButton_4.setText(_translate("trainingQuiz", "PushButton", None))

import resources_rc
