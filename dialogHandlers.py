# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestGameDialog
                                 A QGIS plugin
 test for quiz
                             -------------------
        begin                : 2013-12-19
        copyright            : (C) 2013 by rkrucker
        email                : rafael_krucker@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_files.ui_points import Ui_pointsMessage
from ui_files.ui_trainingQuiz import Ui_trainingQuiz
from ui_files.ui_uberBox import Ui_uberBox
from ui_files.ui_parseFail import Ui_ParseHasFailedDialog
from ui_files.ui_startGame import Ui_testGame
from ui_files.ui_startScreen import Ui_MainWindow


class PointsDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_pointsMessage()
        self.ui.setupUi(self)


class TrainingQuizDialog(QtGui.QDialog):
    def __init__(self, quitMessage):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_trainingQuiz()
        self.ui.setupUi(self)
        self.quitMessage = quitMessage

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(
            self,
            'Message',
            self.quitMessage,
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No
            )

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class UberBoxDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_uberBox()
        self.ui.setupUi(self)


class ParseFailDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_ParseHasFailedDialog()
        self.ui.setupUi(self)


class StartGameDialog(QtGui.QDialog):
    def __init__(self, quitMessage):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_testGame()
        self.ui.setupUi(self)
        self.quitMessage = quitMessage

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(
            self,
            'Message',
            self.quitMessage,
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No
            )

        if reply == QtGui.QMessageBox.Yes:
            self.hide()
        else:
            event.ignore()


class StartScreenDialog(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
