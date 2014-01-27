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
from ui_help import Ui_Hilfe
# create the dialog for zoom to point


class HelpDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Hilfe()
        self.ui.setupUi(self)
