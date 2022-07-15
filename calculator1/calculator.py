
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from image import res
from image.calcu import Ui_Dialog
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys,'_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

uid = Ui_Dialog()

class MainWindow(QDialog,uid):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle("calculator")
        self.btn_1.clicked.connect(self.button_1)
        self.btn_2.clicked.connect(self.button_2)
        self.btn_3.clicked.connect(self.button_3)
        self.btn_4.clicked.connect(self.button_4)
        self.btn_5.clicked.connect(self.button_5)
        self.btn_6.clicked.connect(self.button_6)
        self.btn_7.clicked.connect(self.button_7)
        self.btn_8.clicked.connect(self.button_8)
        self.btn_9.clicked.connect(self.button_9)
        self.btn_0.clicked.connect(self.button_0)
        self.btn_del.clicked.connect(self.del_num)

        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_multiple.clicked.connect(self.multiple)
        self.btn_divide.clicked.connect(self.divide)
        self.btn_result.clicked.connect(self.result)
        # self.btn_percent.clicked.connect(self.percent)
        # self.btn_C.clicked.connect(self.C)
        # self.btn_CE.clicked.connect(self.CE)
        # self.btn_1_x.clicked.connect(self.one_x)
        # self.btn_x_2.clicked.connect(self.x_2)

    # image 처리
    #     self.btn_1.setStyleSheet('border-image:url(./image/1.PNG);border:0px;')
    #     self.btn_2.setStyleSheet('border-image:url(./image/2.PNG);border:0px;')
    #     self.btn_3.setStyleSheet('border-image:url(./image/3.PNG);border:0px;')
    #     self.btn_4.setStyleSheet('border-image:url(./image/4.PNG);border:0px;')
    #     self.btn_5.setStyleSheet('border-image:url(./image/5.PNG);border:0px;')
    #     self.btn_6.setStyleSheet('border-image:url(./image/6.PNG);border:0px;')
    #     self.btn_7.setStyleSheet('border-image:url(./image/7.PNG);border:0px;')
    #     self.btn_8.setStyleSheet('border-image:url(./image/8.PNG);border:0px;')
    #     self.btn_9.setStyleSheet('border-image:url(./image/9.PNG);border:0px;')
    #     self.btn_0.setStyleSheet('border-image:url(./image/0.PNG);border:0px;')
    #     self.btn_plus.setStyleSheet('border-image:url(./image/plus.PNG);border:0px;')
    #     self.btn_minus.setStyleSheet('border-image:url(./image/minus.PNG);border:0px;')
    #     # self.btn_multiple.setStyleSheet('border-image:url(./image/multiple.PNG);border:0px;')
    #     # self.btn_divide.setStyleSheet('border-image:url(./image/divide.PNG);border:0px;')
    #     self.btn_result.setStyleSheet('border-image:url(./image/result.PNG);border:0px;')
    #     self.btn_root.setStyleSheet('border-image:url(./image/root.PNG);border:0px;')


    def button_1(self):
        self.number("1")

    def button_2(self):
        self.number("2")

    def button_3(self):
        self.number("3")

    def button_4(self):
        self.number("4")

    def button_5(self):
        self.number("5")

    def button_6(self):
        self.number("6")

    def button_7(self):
        self.number("7")

    def button_8(self):
        self.number("8")

    def button_9(self):
        self.number("9")

    def button_0(self):
        self.number("0")

    def number(self,num):
        exist_text = self.lineEdit.text() #lineEdit값을 가져와서 exist_text에 저장
        self.lineEdit.setText(exist_text + num) #기존값 + 새로 입력된값

    def del_num(self):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text[:-1])

    def plus(self):
        exist_text = self.lineEdit.text()
        if((exist_text[-1]=="+")|(exist_text[-1]=="-")|(exist_text[-1]=="*")|(exist_text[-1]=="/")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("+")

    def minus(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("-")

    def divide(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("/")

    def multiple(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/")):
            self.lineEdit.setText(exist_text[:-1])
        self.number("*")

    def result(self):
        exist_text = self.lineEdit.text()
        self.number("=")
        try:
            ans = eval(exist_text)
            # self.lineEdit.setText(str(ans))
            self.lineEdit_2.setText(str(ans))
        except Exception as e:
            print(e)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())