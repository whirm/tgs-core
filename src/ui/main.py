# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Feb 29 14:02:55 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 492)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_list = QtGui.QListWidget(self.centralwidget)
        self.message_list.setFrameShape(QtGui.QFrame.NoFrame)
        self.message_list.setFrameShadow(QtGui.QFrame.Plain)
        self.message_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.message_list.setAutoScroll(True)
        self.message_list.setAutoScrollMargin(2)
        self.message_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.message_list.setProperty("showDropIndicator", False)
        self.message_list.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.message_list.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.message_list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.message_list.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.message_list.setMovement(QtGui.QListView.Snap)
        self.message_list.setProperty("isWrapping", False)
        self.message_list.setSpacing(2)
        self.message_list.setWordWrap(True)
        self.message_list.setObjectName("message_list")
        QtGui.QListWidgetItem(self.message_list)
        self.verticalLayout.addWidget(self.message_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nick_line = QtGui.QLineEdit(self.centralwidget)
        self.nick_line.setMaximumSize(QtCore.QSize(60, 16777215))
        self.nick_line.setMaxLength(20)
        self.nick_line.setObjectName("nick_line")
        self.horizontalLayout.addWidget(self.nick_line)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.message_line = QtGui.QLineEdit(self.centralwidget)
        self.message_line.setMaxLength(200)
        self.message_line.setObjectName("message_line")
        self.horizontalLayout.addWidget(self.message_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.message_list.isSortingEnabled()
        self.message_list.setSortingEnabled(False)
        self.message_list.item(0).setText(QtGui.QApplication.translate("MainWindow", "Welcome to TGS Chat Demo!", None, QtGui.QApplication.UnicodeUTF8))
        self.message_list.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nick:", None, QtGui.QApplication.UnicodeUTF8))
        self.nick_line.setText(QtGui.QApplication.translate("MainWindow", "Anon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Message:", None, QtGui.QApplication.UnicodeUTF8))

