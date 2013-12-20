# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_testgame.ui'
#
# Created: Thu Dec 19 14:06:59 2013
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
        TestGame.resize(739, 727)
        TestGame.setStyleSheet(_fromUtf8(""))
        self.widget = QtGui.QWidget(TestGame)
        self.widget.setGeometry(QtCore.QRect(19, -2, 711, 691))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.startTitel = QtGui.QLabel(self.widget)
        self.startTitel.setStyleSheet(_fromUtf8("\n"
"font: italic 24pt \"Verdana\";\n"
"color: rgb(118, 118, 118);"))
        self.startTitel.setObjectName(_fromUtf8("startTitel"))
        self.verticalLayout.addWidget(self.startTitel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startImage = QtGui.QLabel(self.widget)
        self.startImage.setObjectName(_fromUtf8("startImage"))
        self.horizontalLayout.addWidget(self.startImage)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.startGame = QtGui.QPushButton(self.widget)
        self.startGame.setStyleSheet(_fromUtf8("\n"
"font: 12pt \"Verdana\";"))
        self.startGame.setObjectName(_fromUtf8("startGame"))
        self.gridLayout.addWidget(self.startGame, 2, 0, 1, 1)
        self.chooseQuiz = QtGui.QPushButton(self.widget)
        self.chooseQuiz.setStyleSheet(_fromUtf8("font: 12pt \"Verdana\";"))
        self.chooseQuiz.setObjectName(_fromUtf8("chooseQuiz"))
        self.gridLayout.addWidget(self.chooseQuiz, 0, 0, 1, 1)
        self.startTraining = QtGui.QPushButton(self.widget)
        self.startTraining.setStyleSheet(_fromUtf8("font: 12pt \"Verdana\";"))
        self.startTraining.setObjectName(_fromUtf8("startTraining"))
        self.gridLayout.addWidget(self.startTraining, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TestGame)
        QtCore.QMetaObject.connectSlotsByName(TestGame)

    def retranslateUi(self, TestGame):
        TestGame.setWindowTitle(_translate("TestGame", "TestGame", None))
        self.startTitel.setText(_translate("TestGame", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; color:#000000;\">Europa Quiz</span></p></body></html>", None))
        self.startImage.setText(_translate("TestGame", "<html><head/><body><p><img src=\":/newPrefix/europe-map-Start-Page.png\"/></p></body></html>", None))
        self.startGame.setText(_translate("TestGame", "Neues Quiz starten", None))
        self.chooseQuiz.setText(_translate("TestGame", "Quiz auswählen", None))
        self.startTraining.setText(_translate("TestGame", "Training", None))

import resources_rc
