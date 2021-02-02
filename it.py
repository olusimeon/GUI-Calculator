# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'it.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.pushButton_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.pushButton_Clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(190,196,207);\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7)}")
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Plusminu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plusminu.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.pushButton_Plusminu.setStyleSheet("QPushButton {\n"
"  background-color: rgb(190,196,207);\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7)}")
        self.pushButton_Plusminu.setObjectName("pushButton_Plusminu")
        self.pushButton_Percentage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Percentage.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.pushButton_Percentage.setStyleSheet("QPushButton {\n"
"  background-color: rgb(190,196,207);\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7)}")
        self.pushButton_Percentage.setObjectName("pushButton_Percentage")
        self.pushButton_Divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Divide.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.pushButton_Divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_Divide.setObjectName("pushButton_Divide")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_Multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Multiply.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.pushButton_Multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_Multiply.setObjectName("pushButton_Multiply")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_Substract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Substract.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.pushButton_Substract.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_Substract.setObjectName("pushButton_Substract")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_Addition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Addition.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.pushButton_Addition.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_Addition.setObjectName("pushButton_Addition")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_Equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Equal.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.pushButton_Equal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_Equal.setObjectName("pushButton_Equal")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 300, 121, 61))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_Decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Decimal.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.pushButton_Decimal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(190,196,207);\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7)}")
        self.pushButton_Decimal.setObjectName("pushButton_Decimal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_Clear.setText(_translate("MainWindow", "C"))
        self.pushButton_Plusminu.setText(_translate("MainWindow", "+/-"))
        self.pushButton_Percentage.setText(_translate("MainWindow", "%"))
        self.pushButton_Divide.setText(_translate("MainWindow", "/"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_Multiply.setText(_translate("MainWindow", "X"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_Substract.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_Addition.setText(_translate("MainWindow", "+"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_Equal.setText(_translate("MainWindow", "="))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_Decimal.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
