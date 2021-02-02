from PyQt5 import QtWidgets
from it import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber=False



    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # connect numeric button
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        #connect Decimal button
        self.pushButton_Decimal.clicked.connect(self.decimal_pressed)
        
        #connect operator button
        self.pushButton_Plusminu.clicked.connect(self.unary_operation_pressed)
        self.pushButton_Percentage.clicked.connect(self.unary_operation_pressed)

        #connect Operation button
        self.pushButton_Addition.clicked.connect(self.binary_operation_pressed)
        self.pushButton_Substract.clicked.connect(self.binary_operation_pressed)
        self.pushButton_Multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_Divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_Addition.setCheckable(True)
        self.pushButton_Substract.setCheckable(True)
        self.pushButton_Multiply.setCheckable(True)
        self.pushButton_Divide.setCheckable(True)

        # connect equal button
        self.pushButton_Equal.clicked.connect(self.equals_pressed)

        # connect clear button
        self.pushButton_Clear.clicked.connect(self.clear_pressed)

    def digit_pressed(self):
        button = self.sender()

        if ((self.pushButton_Addition.isChecked() or self.pushButton_Substract.isChecked() or
                self.pushButton_Multiply.isChecked() or self.pushButton_Divide.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel= format(float( button.text()), '.15g')
            self.userIsTypingSecondNumber = True

        else:
            if (('.' in self.label.text()) and (button.text() == "0")):
                newLabel = format((self.label.text() + button.text()),'.15g')
            else:
             newLabel = format(float(self.label.text() + button.text()),'.15g')

        self.label.setText(newLabel)


    def decimal_pressed (self) :
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed (self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: # button text == '%'
            labelNumber = labelNumber * 0.01

        newLabel= format(labelNumber, '.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed (self):
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):

        secondNum = float(self.label.text())

        if self.pushButton_Addition.isChecked():
            labelNum = self.firstNum + secondNum
            newLabel= format(labelNum, '.15g')
            self.label.setText(newLabel)
            self.pushButton_Addition.setChecked(False)

        elif self.pushButton_Substract.isChecked():
            labelNum = self.firstNum - secondNum
            newLabel = format(labelNum, '.15g')
            self.label.setText(newLabel)
            self.pushButton_Substract.setChecked(False)

        elif self.pushButton_Multiply.isChecked():
            labelNum = self.firstNum * secondNum
            newLabel = format(labelNum, '.15g')
            self.label.setText(newLabel)
            self.pushButton_Multiply.setChecked(False)

        elif self.pushButton_Divide.isChecked():
            labelNum = self.firstNum / secondNum
            newLabel = format(labelNum, '.15g')
            self.label.setText(newLabel)
            self.pushButton_Divide.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.pushButton_Addition.setChecked(False)
        self.pushButton_Substract.setChecked(False)
        self.pushButton_Multiply.setChecked(False)
        self.pushButton_Divide.setChecked(False)

        self.userIsTypingSecondNumber=False

        self.label.setText("0")

