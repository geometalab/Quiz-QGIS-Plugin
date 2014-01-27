# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_noQuizNote.ui'
#
# Created: Tue Jan 07 10:41:42 2014
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

class Ui_chooseTrainingQuiz(object):
    def setupUi(self, chooseTrainingQuiz):
        chooseTrainingQuiz.setObjectName(_fromUtf8("chooseTrainingQuiz"))
        chooseTrainingQuiz.resize(400, 300)
        self.layoutWidget = QtGui.QWidget(chooseTrainingQuiz)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 321, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.chooseTrainingQuiz = chooseTrainingQuiz		
        self.retranslateUi(chooseTrainingQuiz)
        QtCore.QMetaObject.connectSlotsByName(chooseTrainingQuiz)

    def retranslateUi(self, chooseTrainingQuiz):
        chooseTrainingQuiz.setWindowTitle(_translate("chooseTrainingQuiz", "Wähle ein Quiz", None))
        self.label.setText(_translate("chooseTrainingQuiz", "<html><head/><body><p align=\"center\">Wähle das Quiz aus, welches du trainieren möchtests.</p></body></html>", None))
        self.label_2.setText(_translate("chooseTrainingQuiz", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("chooseTrainingQuiz", "Abbruch", None))
        self.pushButton.setText(_translate("chooseTrainingQuiz", "Quizwahl", None))
        self.pushButton_3.setText(_translate("chooseTrainingQuiz", "Quiz trainieren", None))

