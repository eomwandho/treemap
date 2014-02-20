# -*- coding: utf-8 -*-
"""
/***************************************************************************
 treeMapDialog
                                 A QGIS plugin
 Tree Mapping Tool
                             -------------------
        begin                : 2014-02-20
        copyright            : (C) 2014 by Thomas & Erick
        email                : e.omwandho@gmail.com
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
from ui_treemap import Ui_treeMap
# create the dialog for zoom to point


class treeMapDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_treeMap()
        self.ui.setupUi(self)
