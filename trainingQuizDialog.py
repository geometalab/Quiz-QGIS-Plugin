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
from ui_trainingQuiz import Ui_trainingQuiz
# create the dialog for zoom to point


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
