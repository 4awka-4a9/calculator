from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class DonateWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(DonateWindow, self).__init__(parent)

        self.setWindowTitle("Донат")
        self.setGeometry(300, 250, 300, 300)

        self.BTCtext = QLabel(self)
        self.BTCtext.setGeometry(10, 25, 100, 20)
        self.BTCtext.setText("BTC:")

        self.ETHtext = QLabel(self)
        self.ETHtext.setGeometry(10, 75, 100, 20)
        self.ETHtext.setText("ETH:")

        self.USDTTtext = QLabel(self)
        self.USDTTtext.setGeometry(10, 125, 100, 20)
        self.USDTTtext.setText("USDT TRC 20:")

        self.USDTEtext = QLabel(self)
        self.USDTEtext.setGeometry(10, 175, 100, 20)
        self.USDTEtext.setText("USDT ERC 20:")

        self.BTCcopy = QLineEdit(self)
        self.BTCcopy.setGeometry(10, 50, 270, 20)
        self.BTCcopy.setText("bc1qml9r2f7qud0zsatjf3kh4c6v9yetd8zer52t97")
        self.BTCcopy.setReadOnly(True)

        self.ETHcopy = QLineEdit(self)
        self.ETHcopy.setGeometry(10, 100, 270, 20)
        self.ETHcopy.setText("0xc3006CD922641337053BfB34a919299754002Fa6")
        self.ETHcopy.setReadOnly(True)

        self.USDTTcopy = QLineEdit(self)
        self.USDTTcopy.setGeometry(10, 150, 270, 20)
        self.USDTTcopy.setText("TJ1Zc5Y2SsNLMaQKzdy9XFT5iLAZHx7zGZ")
        self.USDTTcopy.setReadOnly(True)

        self.USDTEcopy = QLineEdit(self)
        self.USDTEcopy.setGeometry(10, 200, 270, 20)
        self.USDTEcopy.setText("0xc3006CD922641337053BfB34a919299754002Fa6")
        self.USDTEcopy.setReadOnly(True)

        self.githubLink = QLabel(self)
        self.githubLink.setGeometry(125, 250, 40, 20)
        self.githubLink.setText("<a href=\"https://github.com/4awka-4a9/weather.git\">github</a>")
        self.githubLink.setOpenExternalLinks(True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 400)
        MainWindow.setMinimumSize(QtCore.QSize(305, 400))
        MainWindow.setMaximumSize(QtCore.QSize(305, 400))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 60, 126, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(5, 5, 220, 70))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(35, 111, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;     ")
        self.resultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.butt1.setGeometry(QtCore.QRect(5, 80, 70, 75))
        self.butt1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt1.setObjectName("butt1")
        self.butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.butt2.setGeometry(QtCore.QRect(80, 80, 70, 75))
        self.butt2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt2.setObjectName("butt2")
        self.butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.butt3.setGeometry(QtCore.QRect(155, 80, 70, 75))
        self.butt3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt3.setObjectName("butt3")
        self.buttPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttPlus.setGeometry(QtCore.QRect(230, 80, 70, 75))
        self.buttPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttPlus.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttPlus.setObjectName("buttPlus")
        self.butt4 = QtWidgets.QPushButton(self.centralwidget)
        self.butt4.setGeometry(QtCore.QRect(5, 160, 70, 75))
        self.butt4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt4.setObjectName("butt4")
        self.butt5 = QtWidgets.QPushButton(self.centralwidget)
        self.butt5.setGeometry(QtCore.QRect(80, 160, 70, 75))
        self.butt5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt5.setObjectName("butt5")
        self.buttMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttMinus.setGeometry(QtCore.QRect(230, 160, 70, 75))
        self.buttMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttMinus.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttMinus.setObjectName("buttMinus")
        self.butt6 = QtWidgets.QPushButton(self.centralwidget)
        self.butt6.setGeometry(QtCore.QRect(155, 160, 70, 75))
        self.butt6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt6.setObjectName("butt6")
        self.butt7 = QtWidgets.QPushButton(self.centralwidget)
        self.butt7.setGeometry(QtCore.QRect(5, 240, 70, 75))
        self.butt7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt7.setObjectName("butt7")
        self.butt8 = QtWidgets.QPushButton(self.centralwidget)
        self.butt8.setGeometry(QtCore.QRect(80, 240, 70, 75))
        self.butt8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt8.setObjectName("butt8")
        self.buttMultiplication = QtWidgets.QPushButton(self.centralwidget)
        self.buttMultiplication.setGeometry(QtCore.QRect(230, 240, 70, 75))
        self.buttMultiplication.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttMultiplication.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttMultiplication.setObjectName("buttMultiplication")
        self.butt9 = QtWidgets.QPushButton(self.centralwidget)
        self.butt9.setGeometry(QtCore.QRect(155, 240, 70, 75))
        self.butt9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt9.setObjectName("butt9")
        self.buttDivision = QtWidgets.QPushButton(self.centralwidget)
        self.buttDivision.setGeometry(QtCore.QRect(230, 320, 70, 75))
        self.buttDivision.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttDivision.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttDivision.setObjectName("buttDivision")
        self.buttEqual = QtWidgets.QPushButton(self.centralwidget)
        self.buttEqual.setGeometry(QtCore.QRect(5, 320, 145, 75))
        self.buttEqual.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttEqual.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttEqual.setObjectName("buttEqual")
        self.butt0 = QtWidgets.QPushButton(self.centralwidget)
        self.butt0.setGeometry(QtCore.QRect(155, 320, 70, 75))
        self.butt0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butt0.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 30pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.butt0.setObjectName("butt0")
        self.buttDonate = QtWidgets.QPushButton(self.centralwidget)
        self.buttDonate.setGeometry(QtCore.QRect(230, 5, 70, 70))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttDonate.setFont(font)
        self.buttDonate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttDonate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(4, 60, 112, 188), stop:1 rgba(255, 255, 255, 255));\n"
"font: 16pt \"PT Sans\";\n"
"color: rgb(0, 56, 94);\n"
"border-radius: 20px;     ")
        self.buttDonate.setObjectName("buttDonate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addFunctions()

        self.isbuttEqual = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resultLabel.setText(_translate("MainWindow", "0"))
        self.butt1.setText(_translate("MainWindow", "1"))
        self.butt2.setText(_translate("MainWindow", "2"))
        self.butt3.setText(_translate("MainWindow", "3"))
        self.buttPlus.setText(_translate("MainWindow", "+"))
        self.butt4.setText(_translate("MainWindow", "4"))
        self.butt5.setText(_translate("MainWindow", "5"))
        self.buttMinus.setText(_translate("MainWindow", "-"))
        self.butt6.setText(_translate("MainWindow", "6"))
        self.butt7.setText(_translate("MainWindow", "7"))
        self.butt8.setText(_translate("MainWindow", "8"))
        self.buttMultiplication.setText(_translate("MainWindow", "×"))
        self.butt9.setText(_translate("MainWindow", "9"))
        self.buttDivision.setText(_translate("MainWindow", "÷"))
        self.buttEqual.setText(_translate("MainWindow", "="))
        self.butt0.setText(_translate("MainWindow", "0"))
        self.buttDonate.setText(_translate("MainWindow", "Donate"))

    def addFunctions(self):
        self.butt0.clicked.connect(lambda: self.writeNum(self.butt0.text()))
        self.butt1.clicked.connect(lambda: self.writeNum(self.butt1.text()))
        self.butt2.clicked.connect(lambda: self.writeNum(self.butt2.text()))
        self.butt3.clicked.connect(lambda: self.writeNum(self.butt3.text()))
        self.butt4.clicked.connect(lambda: self.writeNum(self.butt4.text()))
        self.butt5.clicked.connect(lambda: self.writeNum(self.butt5.text()))
        self.butt6.clicked.connect(lambda: self.writeNum(self.butt6.text()))
        self.butt7.clicked.connect(lambda: self.writeNum(self.butt7.text()))
        self.butt8.clicked.connect(lambda: self.writeNum(self.butt8.text()))
        self.butt9.clicked.connect(lambda: self.writeNum(self.butt9.text()))

        self.buttPlus.clicked.connect(lambda: self.writeNum("+"))
        self.buttMinus.clicked.connect(lambda: self.writeNum("-"))
        self.buttDivision.clicked.connect(lambda: self.writeNum("/"))
        self.buttMultiplication.clicked.connect(lambda: self.writeNum("*"))

        self.buttEqual.clicked.connect(self.result)

        self.buttDonate.clicked.connect(self.show_donate_menu)


    def writeNum(self, number):
        if self.resultLabel.text() == "0" or self.isbuttEqual == True:
            self.resultLabel.setText(number)
            self.isbuttEqual = False
        else:
            self.resultLabel.setText(self.resultLabel.text() + number )


    def result(self):
        try:
            res = eval(self.resultLabel.text())
            self.resultLabel.setText(str(float(res)))
        except:
            self.resultLabel.setText("ERROR")
        self.isbuttEqual = True

    def show_donate_menu(self):
        pass
        self.donate = DonateWindow()
        self.donate.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
