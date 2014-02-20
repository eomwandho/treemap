# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_treemap.ui'
#
# Created: Thu Feb 20 10:03:35 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_treeMap(object):
    def setupUi(self, treeMap):
        treeMap.setObjectName(_fromUtf8("treeMap"))
        treeMap.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(treeMap)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(treeMap)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), treeMap.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), treeMap.reject)
        QtCore.QMetaObject.connectSlotsByName(treeMap)

    def retranslateUi(self, treeMap):
        treeMap.setWindowTitle(QtGui.QApplication.translate("treeMap", "treeMap", None, QtGui.QApplication.UnicodeUTF8))

