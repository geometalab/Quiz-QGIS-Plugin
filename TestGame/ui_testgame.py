# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_testgame.ui'
#
# Created: Thu Jan 23 16:24:43 2014
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

class Ui_TestGame(object):
    def setupUi(self, TestGame):
        TestGame.setObjectName(_fromUtf8("TestGame"))
        TestGame.resize(607, 381)
        TestGame.setStyleSheet(_fromUtf8(""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(TestGame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.startTitel = QtGui.QLabel(TestGame)
        self.startTitel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.startTitel.setStyleSheet(_fromUtf8("\n"
"font: italic 24pt \"Verdana\";\n"
"color: rgb(118, 118, 118);"))
        self.startTitel.setObjectName(_fromUtf8("startTitel"))
        self.horizontalLayout_3.addWidget(self.startTitel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startImage = QtGui.QLabel(TestGame)
        self.startImage.setObjectName(_fromUtf8("startImage"))
        self.horizontalLayout.addWidget(self.startImage)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.startGame = QtGui.QPushButton(TestGame)
        self.startGame.setStyleSheet(_fromUtf8("\n"
"font: 12pt \"Verdana\";"))
        self.startGame.setText(_fromUtf8(""))
        self.startGame.setObjectName(_fromUtf8("startGame"))
        self.verticalLayout.addWidget(self.startGame)
        self.startTraining = QtGui.QPushButton(TestGame)
        self.startTraining.setStyleSheet(_fromUtf8("font: 12pt \"Verdana\";"))
        self.startTraining.setText(_fromUtf8(""))
        self.startTraining.setObjectName(_fromUtf8("startTraining"))
        self.verticalLayout.addWidget(self.startTraining)
        self.chooseQuiz = QtGui.QPushButton(TestGame)
        self.chooseQuiz.setStyleSheet(_fromUtf8("font: 12pt \"Verdana\";"))
        self.chooseQuiz.setText(_fromUtf8(""))
        self.chooseQuiz.setObjectName(_fromUtf8("chooseQuiz"))
        self.verticalLayout.addWidget(self.chooseQuiz)
        self.pushButton = QtGui.QPushButton(TestGame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 73, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(TestGame)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtGui.QPushButton(TestGame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(TestGame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label = QtGui.QLabel(TestGame)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(TestGame)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TestGame)
        QtCore.QMetaObject.connectSlotsByName(TestGame)

    def retranslateUi(self, TestGame):
        TestGame.setWindowTitle(_translate("TestGame", "TestGame", None))
        self.startTitel.setText(_translate("TestGame", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:normal; color:#000000;\">Quiz</span></p></body></html>", None))
        self.startImage.setText(_translate("TestGame", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("TestGame", "-", None))
        self.pushButton_3.setText(_translate("TestGame", "+", None))
        self.comboBox.setItemText(0, _translate("TestGame", "Deutsch", None))
        self.comboBox.setItemText(1, _translate("TestGame", "English", None))

import resources_rc
