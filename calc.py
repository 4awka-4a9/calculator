from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 370)
        self.resultLabel = QtWidgets.QLabel(Dialog)
        self.resultLabel.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("background-color: rgb(159, 137, 173);")
        self.resultLabel.setObjectName("resultLabel")
        self.but1 = QtWidgets.QPushButton(Dialog)
        self.but1.setGeometry(QtCore.QRect(0, 50, 80, 80))
        self.but1.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but1.setObjectName("but1")
        self.but2 = QtWidgets.QPushButton(Dialog)
        self.but2.setGeometry(QtCore.QRect(80, 50, 80, 80))
        self.but2.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but2.setObjectName("but2")
        self.but3 = QtWidgets.QPushButton(Dialog)
        self.but3.setGeometry(QtCore.QRect(160, 50, 80, 80))
        self.but3.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but3.setObjectName("but3")
        self.but4 = QtWidgets.QPushButton(Dialog)
        self.but4.setGeometry(QtCore.QRect(0, 130, 80, 80))
        self.but4.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but4.setObjectName("but4")
        self.but5 = QtWidgets.QPushButton(Dialog)
        self.but5.setGeometry(QtCore.QRect(80, 130, 80, 80))
        self.but5.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but5.setObjectName("but5")
        self.but6 = QtWidgets.QPushButton(Dialog)
        self.but6.setGeometry(QtCore.QRect(160, 130, 80, 80))
        self.but6.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but6.setObjectName("but6")
        self.but7 = QtWidgets.QPushButton(Dialog)
        self.but7.setGeometry(QtCore.QRect(0, 210, 80, 80))
        self.but7.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but7.setObjectName("but7")
        self.but8 = QtWidgets.QPushButton(Dialog)
        self.but8.setGeometry(QtCore.QRect(80, 210, 80, 80))
        self.but8.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but8.setObjectName("but8")
        self.but9 = QtWidgets.QPushButton(Dialog)
        self.but9.setGeometry(QtCore.QRect(160, 210, 80, 80))
        self.but9.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but9.setObjectName("but9")
        self.but0 = QtWidgets.QPushButton(Dialog)
        self.but0.setGeometry(QtCore.QRect(0, 290, 150, 80))
        self.but0.setStyleSheet("background-color: rgb(167, 255, 132);")
        self.but0.setObjectName("but0")
        self.butReturn = QtWidgets.QPushButton(Dialog)
        self.butReturn.setGeometry(QtCore.QRect(150, 290, 150, 80))
        self.butReturn.setStyleSheet("background-color: rgb(126, 255, 240);")
        self.butReturn.setObjectName("butReturn")
        self.butPlus = QtWidgets.QPushButton(Dialog)
        self.butPlus.setGeometry(QtCore.QRect(240, 50, 60, 60))
        self.butPlus.setStyleSheet("background-color: rgb(255, 181, 100);")
        self.butPlus.setObjectName("butPlus")
        self.butMinus = QtWidgets.QPushButton(Dialog)
        self.butMinus.setGeometry(QtCore.QRect(240, 110, 60, 60))
        self.butMinus.setStyleSheet("background-color: rgb(255, 181, 100);")
        self.butMinus.setObjectName("butMinus")
        self.butDiv = QtWidgets.QPushButton(Dialog)
        self.butDiv.setGeometry(QtCore.QRect(240, 170, 60, 60))
        self.butDiv.setStyleSheet("background-color: rgb(255, 181, 100);")
        self.butDiv.setObjectName("butDiv")
        self.butMult = QtWidgets.QPushButton(Dialog)
        self.butMult.setGeometry(QtCore.QRect(240, 230, 60, 60))
        self.butMult.setStyleSheet("background-color: rgb(255, 181, 100);")
        self.butMult.setObjectName("butMult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addFunctions()

        self.isEqual = False

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.resultLabel.setText(_translate("Dialog", "0"))
        self.but1.setText(_translate("Dialog", "1"))
        self.but2.setText(_translate("Dialog", "2"))
        self.but3.setText(_translate("Dialog", "3"))
        self.but4.setText(_translate("Dialog", "4"))
        self.but5.setText(_translate("Dialog", "5"))
        self.but6.setText(_translate("Dialog", "6"))
        self.but7.setText(_translate("Dialog", "7"))
        self.but8.setText(_translate("Dialog", "8"))
        self.but9.setText(_translate("Dialog", "9"))
        self.but0.setText(_translate("Dialog", "0"))
        self.butReturn.setText(_translate("Dialog", "="))
        self.butPlus.setText(_translate("Dialog", "+"))
        self.butMinus.setText(_translate("Dialog", "-"))
        self.butDiv.setText(_translate("Dialog", "*"))
        self.butMult.setText(_translate("Dialog", "/"))

    def addFunctions(self):
        self.but0.clicked.connect(lambda: self.writeNum(self.but0.text()))
        self.but1.clicked.connect(lambda: self.writeNum(self.but1.text()))
        self.but2.clicked.connect(lambda: self.writeNum(self.but2.text()))
        self.but3.clicked.connect(lambda: self.writeNum(self.but3.text()))
        self.but4.clicked.connect(lambda: self.writeNum(self.but4.text()))
        self.but5.clicked.connect(lambda: self.writeNum(self.but5.text()))
        self.but6.clicked.connect(lambda: self.writeNum(self.but6.text()))
        self.but7.clicked.connect(lambda: self.writeNum(self.but7.text()))
        self.but8.clicked.connect(lambda: self.writeNum(self.but8.text()))
        self.but9.clicked.connect(lambda: self.writeNum(self.but9.text()))

        self.butPlus.clicked.connect(lambda: self.writeNum(self.butPlus.text()))
        self.butMinus.clicked.connect(lambda: self.writeNum(self.butMinus.text()))
        self.butDiv.clicked.connect(lambda: self.writeNum(self.butDiv.text()))
        self.butMult.clicked.connect(lambda: self.writeNum(self.butMult.text()))

        self.butReturn.clicked.connect(self.result)


    def writeNum(self, number):
        print(number)
        if self.resultLabel.text() == "0" or self.isEqual == True:
            self.resultLabel.setText(number)
            self.isEqual = False
        else:
            self.resultLabel.setText(self.resultLabel.text() + number )

    def result(self):
        try:
            res = eval(self.resultLabel.text())
            self.resultLabel.setText(str(int(res)))
        except:
            self.resultLabel.setText("ERROR")



        self.isEqual = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
