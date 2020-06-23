# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Text_editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        TextEditor.setObjectName("TextEditor")
        TextEditor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TextEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.plainTextEdit.setObjectName("plainTextEdit")
        TextEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TextEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        TextEditor.setMenuBar(self.menubar)
        self.actionFont_size = QtWidgets.QAction(TextEditor)
        self.actionFont_size.setObjectName("actionFont_size")
        self.actionFont_color = QtWidgets.QAction(TextEditor)
        self.actionFont_color.setObjectName("actionFont_color")
        self.actionFont_Style = QtWidgets.QAction(TextEditor)
        self.actionFont_Style.setObjectName("actionFont_Style")
        self.actionNew = QtWidgets.QAction(TextEditor)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(TextEditor)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(TextEditor)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(TextEditor)
        self.actionExit.setObjectName("actionExit")
        self.actionFormatsettings=QtWidgets.QAction(TextEditor)
        self.actionFormatsettings.setObjectName('actionFormatSettings')
        self.actionFormatsettings.setText('Text Formatting')
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)

        # self.menuEdit.addAction(self.actionFont_size)
        # self.menuEdit.addAction(self.actionFont_color)
        # self.menuEdit.addAction(self.actionFont_Style)
        self.menuEdit.addAction(self.actionFormatsettings)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(TextEditor)
        QtCore.QMetaObject.connectSlotsByName(TextEditor)

    def retranslateUi(self, TextEditor):
        _translate = QtCore.QCoreApplication.translate
        TextEditor.setWindowTitle(_translate("TextEditor", "Text Editor"))
        self.menuFile.setTitle(_translate("TextEditor", "File"))
        self.menuEdit.setTitle(_translate("TextEditor", "Edit"))
        self.actionFont_size.setText(_translate("TextEditor", "Font size"))
        self.actionFont_color.setText(_translate("TextEditor", "Font color"))
        self.actionFont_Style.setText(_translate("TextEditor", "Font Style"))
        self.actionNew.setText(_translate("TextEditor", "New"))
        self.actionOpen.setText(_translate("TextEditor", "Open"))
        self.actionSave.setText(_translate("TextEditor", "Save"))
        self.actionExit.setText(_translate("TextEditor", "Exit"))
