# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_box.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_format_box(object):
    def setupUi(self, format_box):
        format_box.setObjectName("format_box")
        format_box.resize(361, 441)
        self.label = QtWidgets.QLabel(format_box)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(format_box)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(format_box)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 151, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(format_box)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 90, 181, 22))
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(48)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.spinBox = QtWidgets.QSpinBox(format_box)
        self.spinBox.setGeometry(QtCore.QRect(260, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(48)
        self.spinBox.setObjectName("spinBox")
        self.line = QtWidgets.QFrame(format_box)
        self.line.setGeometry(QtCore.QRect(0, 50, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(format_box)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 351, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(format_box)
        self.line_3.setGeometry(QtCore.QRect(0, 310, 351, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.color_picker = QtWidgets.QPushButton(format_box)
        self.color_picker.setGeometry(QtCore.QRect(20, 200, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color_picker.setFont(font)
        self.color_picker.setObjectName("color_picker")
        self.font_picker = QtWidgets.QFontComboBox(format_box)
        self.font_picker.setGeometry(QtCore.QRect(20, 340, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.font_picker.setCurrentFont(font)
        self.font_picker.setObjectName("font_picker")
        self.cancel_btn = QtWidgets.QPushButton(format_box)
        self.cancel_btn.setGeometry(QtCore.QRect(10, 390, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.apply_btn = QtWidgets.QPushButton(format_box)
        self.apply_btn.setGeometry(QtCore.QRect(260, 390, 93, 28))
        self.apply_btn.setObjectName("apply_btn")

        self.retranslateUi(format_box)
        self.horizontalSlider.valueChanged['int'].connect(self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(format_box)

    def retranslateUi(self, format_box):
        _translate = QtCore.QCoreApplication.translate
        format_box.setWindowTitle(_translate("format_box", "Text Formatting"))
        self.label.setText(_translate("format_box", "Font size:"))
        self.label_2.setText(_translate("format_box", "Font color:"))
        self.label_3.setText(_translate("format_box", "Font Style:"))
        self.color_picker.setText(_translate("format_box", "Pick a color"))
        self.cancel_btn.setText(_translate("format_box", "Cancel"))
        self.apply_btn.setText(_translate("format_box", "Apply"))


class Ui_format_box_deriverd(QDialog, Ui_format_box):
    def __init__(self):
        super(Ui_format_box_deriverd, self).__init__()
        """finsih this shit"""
        # self.show()

