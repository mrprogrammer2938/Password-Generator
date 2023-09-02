#!/usr/bin/python3
# This App Made By Sina Meysami
# Password Generator v1.0
#
#
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import qdarktheme
import sys,random,platform,webbrowser

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        qdarktheme.setup_theme("dark")
        loadUi("form.ui",self)
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(600,200,381,560)
        self.setFixedSize(381,560)
        
        # Menu
        self.save_pass_action.triggered.connect(self.save_password)
        self.exit_action.triggered.connect(self.close)
        
        self.spin.setMinimum(6)
        self.spin.setMaximum(50)
        self.spin.setValue(8)
        self.spin.setSingleStep(1)
        self.spin.setPrefix("Length: ")
        # Buttons
        self.generate_btn.clicked.connect(self.generate)
        self.ads_btn.clicked.connect(self.ads)
        #self.copy_btn.clicked.connect(self.copy_text)
        #self.clear_btn.clicked.connect(self.text.clear)
    def generate(self):
        try:
            num = self.spin.value()
            PASS = ""
            if self.check_line.isChecked() == True:
                text = self.line.text()
                PASS += text
            else:
                PASS += ""
            if self.check_1.isChecked() == True:
                PASS += "ABSCDEFGHIJKLMNOPQRSTUVWXYZ"
            else:
                PASS += ""
            if self.check_2.isChecked() == True:
                PASS += "abcdefghijklmnopqrstuvwxyz"
            else:
                PASS += ""
            if self.check_3.isChecked() == True:
                PASS += "!@#$%^&*()+"
            else:
                PASS += ""
            if self.check_4.isChecked() == True:
                PASS += "1234567890"
            else:
                PASS += ""
            if self.check_5.isChecked() == True:
                PASS += "~`[];?,"
            else:
                PASS += ""
            for i in range(num):
                n = random.sample(PASS,num)
                n2 = "".join(n)
                self.text.setText(n2)
        except:
            mess = QMessageBox(self)
            mess.setWindowTitle("Password Generator/Error")
            mess.resize(100,50)
            mess.setText("Error")
            mess.exec_()
    def save_password(self):
        file_pass = QFileDialog().getSaveFileName(self,"Open File","C:\\","Text Files (*.txt)")
        with open(file_pass[0],"w") as file:
            file.write(self.text.toPlainText())
    def ads(self):
        webbrowser.open_new_tab("mailto:sinameysami@gmail.com")
    def copy_text(self):
        self.text.selectAll()
        self.text.copy()   
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Password Generator")
    app.setApplicationVersion("1")
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        main()
    else:
        print("Please, Run This App On Windows,Linux,Mac OS!")
        sys.exit()
    