# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trainingQuiz.ui'
#
# Created: Mon Feb 10 12:56:27 2014
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
        trainingQuiz.resize(596, 693)
        trainingQuiz.setAutoFillBackground(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(trainingQuiz)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(trainingQuiz)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_6 = QtGui.QLabel(trainingQuiz)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.stackedWidget_2 = QtGui.QStackedWidget(trainingQuiz)
        self.stackedWidget_2.setObjectName(_fromUtf8("stackedWidget_2"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(17, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.page_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.page_3)
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(self.page_3)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 6, 1)
        self.pushButton_2 = QtGui.QPushButton(self.page_3)
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.page_3)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.page_3)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.page_3)
        self.pushButton_5.setStyleSheet(_fromUtf8(""))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.page_3)
        self.pushButton_6.setStyleSheet(_fromUtf8(""))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 4, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 3, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.page_3)
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.page_3)
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 3, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 3, 4, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 0, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.page_3)
        self.pushButton_9.setStyleSheet(_fromUtf8(""))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 4, 1, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.page_3)
        self.pushButton_10.setStyleSheet(_fromUtf8(""))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 4, 3, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 4, 4, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 0, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.page_3)
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 5, 1, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.page_3)
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 5, 3, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 5, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.page_4)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.labelGap = QtGui.QLabel(self.page_4)
        self.labelGap.setWordWrap(True)
        self.labelGap.setObjectName(_fromUtf8("labelGap"))
        self.horizontalLayout_17.addWidget(self.labelGap)
        spacerItem16 = QtGui.QSpacerItem(244, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem16)
        self.line = QtGui.QFrame(self.page_4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_17.addWidget(self.line)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.editLabel = QtGui.QLabel(self.page_4)
        self.editLabel.setObjectName(_fromUtf8("editLabel"))
        self.horizontalLayout_5.addWidget(self.editLabel)
        self.lineEditGap = QtGui.QLineEdit(self.page_4)
        self.lineEditGap.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap.setObjectName(_fromUtf8("lineEditGap"))
        self.horizontalLayout_5.addWidget(self.lineEditGap)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.editLabel_2 = QtGui.QLabel(self.page_4)
        self.editLabel_2.setObjectName(_fromUtf8("editLabel_2"))
        self.horizontalLayout_6.addWidget(self.editLabel_2)
        self.lineEditGap_2 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_2.setObjectName(_fromUtf8("lineEditGap_2"))
        self.horizontalLayout_6.addWidget(self.lineEditGap_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.editLabel_3 = QtGui.QLabel(self.page_4)
        self.editLabel_3.setObjectName(_fromUtf8("editLabel_3"))
        self.horizontalLayout_7.addWidget(self.editLabel_3)
        self.lineEditGap_3 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_3.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_3.setObjectName(_fromUtf8("lineEditGap_3"))
        self.horizontalLayout_7.addWidget(self.lineEditGap_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.editLabel_4 = QtGui.QLabel(self.page_4)
        self.editLabel_4.setObjectName(_fromUtf8("editLabel_4"))
        self.horizontalLayout_8.addWidget(self.editLabel_4)
        self.lineEditGap_4 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_4.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_4.setObjectName(_fromUtf8("lineEditGap_4"))
        self.horizontalLayout_8.addWidget(self.lineEditGap_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.editLabel_5 = QtGui.QLabel(self.page_4)
        self.editLabel_5.setObjectName(_fromUtf8("editLabel_5"))
        self.horizontalLayout_9.addWidget(self.editLabel_5)
        self.lineEditGap_5 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_5.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_5.setObjectName(_fromUtf8("lineEditGap_5"))
        self.horizontalLayout_9.addWidget(self.lineEditGap_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.editLabel_6 = QtGui.QLabel(self.page_4)
        self.editLabel_6.setObjectName(_fromUtf8("editLabel_6"))
        self.horizontalLayout_10.addWidget(self.editLabel_6)
        self.lineEditGap_6 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_6.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_6.setObjectName(_fromUtf8("lineEditGap_6"))
        self.horizontalLayout_10.addWidget(self.lineEditGap_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.editLabel_7 = QtGui.QLabel(self.page_4)
        self.editLabel_7.setObjectName(_fromUtf8("editLabel_7"))
        self.horizontalLayout_11.addWidget(self.editLabel_7)
        self.lineEditGap_7 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_7.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_7.setObjectName(_fromUtf8("lineEditGap_7"))
        self.horizontalLayout_11.addWidget(self.lineEditGap_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.editLabel_8 = QtGui.QLabel(self.page_4)
        self.editLabel_8.setObjectName(_fromUtf8("editLabel_8"))
        self.horizontalLayout_12.addWidget(self.editLabel_8)
        self.lineEditGap_8 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_8.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_8.setObjectName(_fromUtf8("lineEditGap_8"))
        self.horizontalLayout_12.addWidget(self.lineEditGap_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.editLabel_9 = QtGui.QLabel(self.page_4)
        self.editLabel_9.setObjectName(_fromUtf8("editLabel_9"))
        self.horizontalLayout_13.addWidget(self.editLabel_9)
        self.lineEditGap_9 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_9.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_9.setObjectName(_fromUtf8("lineEditGap_9"))
        self.horizontalLayout_13.addWidget(self.lineEditGap_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.editLabel_10 = QtGui.QLabel(self.page_4)
        self.editLabel_10.setObjectName(_fromUtf8("editLabel_10"))
        self.horizontalLayout_14.addWidget(self.editLabel_10)
        self.lineEditGap_10 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_10.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_10.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_10.setObjectName(_fromUtf8("lineEditGap_10"))
        self.horizontalLayout_14.addWidget(self.lineEditGap_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.editLabel_11 = QtGui.QLabel(self.page_4)
        self.editLabel_11.setObjectName(_fromUtf8("editLabel_11"))
        self.horizontalLayout_15.addWidget(self.editLabel_11)
        self.lineEditGap_11 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_11.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_11.setObjectName(_fromUtf8("lineEditGap_11"))
        self.horizontalLayout_15.addWidget(self.lineEditGap_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.editLabel_12 = QtGui.QLabel(self.page_4)
        self.editLabel_12.setObjectName(_fromUtf8("editLabel_12"))
        self.horizontalLayout_16.addWidget(self.editLabel_12)
        self.lineEditGap_12 = QtGui.QLineEdit(self.page_4)
        self.lineEditGap_12.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditGap_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditGap_12.setObjectName(_fromUtf8("lineEditGap_12"))
        self.horizontalLayout_16.addWidget(self.lineEditGap_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.horizontalLayout_17.addLayout(self.verticalLayout_4)
        self.stackedWidget_2.addWidget(self.page_4)
        self.verticalLayout_3.addWidget(self.stackedWidget_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 20, -1, 20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(trainingQuiz)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(trainingQuiz)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(trainingQuiz)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem19)
        self.pushButton_13 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_13.setText(_fromUtf8(""))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.horizontalLayout.addWidget(self.pushButton_13)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_14 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_14.setText(_fromUtf8(""))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem21)
        self.pushButton_16 = QtGui.QPushButton(trainingQuiz)
        self.pushButton_16.setText(_fromUtf8(""))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_2.addWidget(self.pushButton_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(trainingQuiz)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(trainingQuiz)

    def retranslateUi(self, trainingQuiz):
        trainingQuiz.setWindowTitle(_translate("trainingQuiz", "Training", None))
        self.label.setText(_translate("trainingQuiz", "<html><head/><body><p><br/></p></body></html>", None))
        self.labelGap.setText(_translate("trainingQuiz", "TextLabel", None))
        self.editLabel.setText(_translate("trainingQuiz", "1", None))
        self.editLabel_2.setText(_translate("trainingQuiz", "2", None))
        self.editLabel_3.setText(_translate("trainingQuiz", "3", None))
        self.editLabel_4.setText(_translate("trainingQuiz", "4", None))
        self.editLabel_5.setText(_translate("trainingQuiz", "5", None))
        self.editLabel_6.setText(_translate("trainingQuiz", "6", None))
        self.editLabel_7.setText(_translate("trainingQuiz", "7", None))
        self.editLabel_8.setText(_translate("trainingQuiz", "8", None))
        self.editLabel_9.setText(_translate("trainingQuiz", "9", None))
        self.editLabel_10.setText(_translate("trainingQuiz", "10", None))
        self.editLabel_11.setText(_translate("trainingQuiz", "11", None))
        self.editLabel_12.setText(_translate("trainingQuiz", "12", None))

import resources_rc
