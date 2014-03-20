from PyQt4 import QtCore, QtGui
from ui_parseFail import Ui_ParseHasFailedDialog
# create the dialog for zoom to point


class ParseFailDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_ParseHasFailedDialog()
        self.ui.setupUi(self)

