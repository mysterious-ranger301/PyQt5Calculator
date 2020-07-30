# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:33:55 2020

@author: Mysterious Ranger
A simple calculator using PyQt5
"""

from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow # you need to have it in the cdir
import sys # for sys.exit

class main(Ui_MainWindow, QMainWindow): # main window
    def __init__(self, parent=None): # set parent=None for the superclass __init__
        super().__init__(parent) # here's why
        self.setupUi(self) # setupUi defined in Ui_MainWindow
        self.b1.clicked.connect(self.b1Action) # oh, here the pain begins...
        self.b2.clicked.connect(self.b2Action)
        self.b3.clicked.connect(self.b3Action)
        self.b4.clicked.connect(self.b4Action) # we there yet?
        self.b5.clicked.connect(self.b5Action)
        self.b6.clicked.connect(self.b6Action)
        self.b7.clicked.connect(self.b7Action) # oh, my fingers...
        self.b8.clicked.connect(self.b8Action)
        self.b9.clicked.connect(self.b9Action)
        self.b0.clicked.connect(self.b0Action) # thank god... NOOOOO!!! THE
        # OPERATORS!!!
        self.bPlus.clicked.connect(self.plus)
        self.bMinus.clicked.connect(self.minus)
        self.bTimes.clicked.connect(self.times)
        self.bDivide.clicked.connect(self.divide) # yess, finally...
        
        self.mainLineEdit.editingFinished.connect(self.evaluate)
        self.clearButton.clicked.connect(lambda: self.mainLineEdit.clear())
        self.exitButton.clicked.connect(lambda: sys.exit())
        self.resultButton.clicked.connect(self.evaluate)
        
        self.setWindowTitle('PyQt5 Calculator')
        self.show() # show the window
        # TODO: Create the methods for buttons (more finger pain!)
    def b0Action(self): # ohhh no...
        text = self.mainLineEdit.text() # don't change the previous text
        text += '0'
        self.mainLineEdit.setText(text) # so... this is how we'll do it
    def b1Action(self):
        text = self.mainLineEdit.text()
        text += '1'
        self.mainLineEdit.setText(text) # OK... I'm gonna copy & paste here...
    def b2Action(self):
        text = self.mainLineEdit.text()
        text += '2'
        self.mainLineEdit.setText(text)
    def b3Action(self):
        text = self.mainLineEdit.text()
        text += '3'
        self.mainLineEdit.setText(text)
    def b4Action(self):
        text = self.mainLineEdit.text()
        text += '4'
        self.mainLineEdit.setText(text)
    def b5Action(self):
        text = self.mainLineEdit.text()
        text += '5'
        self.mainLineEdit.setText(text)
    def b6Action(self):
        text = self.mainLineEdit.text()
        text += '6'
        self.mainLineEdit.setText(text)
    def b7Action(self):
        text = self.mainLineEdit.text()
        text += '7'
        self.mainLineEdit.setText(text) # we're only on b7... yikes!
    def b8Action(self):
        text = self.mainLineEdit.text()
        text += '8'
        self.mainLineEdit.setText(text)
    def b9Action(self):
        text = self.mainLineEdit.text()
        text += '9'
        self.mainLineEdit.setText(text)
    # OK, all of the numButton functions
    # TODO: Create the operator functions
    def plus(self):
        text = self.mainLineEdit.text()
        text += '+'
        self.mainLineEdit.setText(text) # gonna do the same thing here
    def minus(self):
        text = self.mainLineEdit.text()
        text += '-'
        self.mainLineEdit.setText(text)
    def times(self):
        text = self.mainLineEdit.text()
        text += '*'
        self.mainLineEdit.setText(text)
    def divide(self):
        text = self.mainLineEdit.text()
        text += '/'
        self.mainLineEdit.setText(text)
    # TODO: Now make the evaluate method
    def evaluate(self):
        # OK, so we'll use exec to execute the text
        # The text is from the line edit
        text = self.mainLineEdit.text() # get the text
        try: # put this in a try statement...
            exec('result = {0}'.format(text)) # so we execute the expression...
            exec('self.mainLineEdit.setText(str(result))') # ... and if it's valid, we set it to the text
            # it only works in exec() itself
        except Exception as e:
            msg = QMessageBox()
            msg.setText('Oops, an error has occured:\n{0}'.format(e))
            msg.exec() # inform the user that an error has occured
            self.mainLineEdit.clear() # clear the current text
if __name__ == '__main__':
    app = QApplication([])
    window = main()
    app.exec()
