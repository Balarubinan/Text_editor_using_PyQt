from PyQt5.QtGui import QTextCursor, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QColorDialog, QTextEdit
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtGui
from os import sys
import pickle

from source.UI_files.text_editor_UI import Ui_TextEditor
from source.UI_files.format_box_UI import Ui_format_box_deriverd,Ui_format_box


class app_window(Ui_TextEditor, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.file = None  # t hold the current opened file if required
        self.msg = QMessageBox()  # message box to hold messages
        self.font_settings = QtGui.QFont()  # holds all the formating so far applied
        self.actionOpen.triggered.connect(self.open_file)
        self.actionExit.triggered.connect(self.exit)
        self.actionNew.triggered.connect(self.create_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionFormatsettings.triggered.connect(self.format_box)

        # format box actions
        self.win = QDialog()
        self.obj = Ui_format_box()
        self.obj.setupUi(self.win)
        self.obj.apply_btn.clicked.connect(self.set_params)
        self.obj.color_picker.clicked.connect(self.change_color)
        self.obj.cancel_btn.clicked.connect(self.close_format)

        # other
        self.openDiaglist=[]

    def close_format(self):
        """closes the format box"""
        self.win.hide()
        self.win.destroy()

    def display_message(self, title='', message='Default'):
        """Displays a pop-up message to the user using given title and messgae strings"""
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
        self.msg.exec()

    def save_file(self):
        """ saves the QTextDocument object using the pickle object serialization """
        doc=self.plainTextEdit.document()
        name,j=QFileDialog.getSaveFileName(self,'Save Dialog','Untitled')
        doc_html=doc.toHtml()
        pickle.dump(doc_html,open(f'{name}.rtxt','wb'))
        self.display_message('Text saved','Text Document saved successfully')

    def create_file(self):
        # self.save_file()
        self.display_message('Save File','Please Save Current file to open a new file')
        self.save_file()
        self.plainTextEdit.setPlainText('')
        self.display_message('New file',"New File Created")

    def exit(self):
        self.hide()
        sys.exit(0)

    def open_file(self):
        """Loads a file into the PlainTextEdit Qwidget"""
        file_name, j = QFileDialog.getOpenFileName(self, 'Select Text file', '/home')
        if file_name.endswith('rtxt'):
            file = pickle.load(open(file_name,'rb'))
            self.new_doc=QTextDocument()
            self.new_doc.setHtml(file)
            self.plainTextEdit.setDocument(self.new_doc)

        elif file_name is None:  # happens when use cancels dialog
            self.display_message('No file','No file selected')
        else:
            self.display_message('Error', 'Wrong format selected . please Choose txt files')

    def change_font_size(self, font_size=22):
        """This fucntion changes the font_size of the text for the hole editor"""
        self.font_settings.setPointSize(font_size)
        self.plainTextEdit.setFont(self.font_settings)

    def change_font_style(self, font_style):
        """This fucntion changes the font_style of the text for the hole editor"""
        self.font_settings.setStyle(font_style)
        self.plainTextEdit.setFont(self.font_settings)

    def change_color(self,color):
        color=QColorDialog.getColor()
        self.display_message('selected color is',color.name())
        self.plainTextEdit.setTextColor(color)

    def format_box(self):
        """This function is to display a format edit box for the editor"""
        self.win.setFocus()
        self.win.exec_()

    def set_params(self):
        """Set the parmaters once the Apply buttonn is clicked"""
        font_size=self.obj.spinBox.value()
        font_style=self.obj.font_picker.currentFont().style()
        font_color=self.obj.color_picker.colorCount()
        self.change_font_size(font_size)
        self.change_font_style(font_style)

app = QApplication([])
w = app_window()
sys.exit(app.exec_())
