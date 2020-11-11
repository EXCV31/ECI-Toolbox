from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from string import Template
import shutil
import ctypes
import time

desktop_path = os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\'))

class Ui_cps_generator_window(object):
    def setupUi(self, cps_generator_window):
        cps_generator_window.setObjectName("cps_generator_window")
        cps_generator_window.resize(1018, 681)
        cps_generator_window.setWindowIcon(QIcon('transfer.png'))
        self.centralwidget = QtWidgets.QWidget(cps_generator_window)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(50, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(20)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(830, 560, 151, 51))
        self.generate_button.setObjectName("generate_button")
        self.send_to_printer_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_to_printer_button.setGeometry(QtCore.QRect(620, 560, 151, 51))
        self.send_to_printer_button.setObjectName("send_to_printer_button")
        self.emp_code_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_code_label.setGeometry(QtCore.QRect(130, 210, 181, 34))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.emp_code_label.setFont(font)
        self.emp_code_label.setObjectName("emp_code_label")
        self.full_name_label = QtWidgets.QLabel(self.centralwidget)
        self.full_name_label.setGeometry(QtCore.QRect(130, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.full_name_label.setFont(font)
        self.full_name_label.setObjectName("full_name_label")
        self.emp_code_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_code_entry.setGeometry(QtCore.QRect(530, 210, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.emp_code_entry.setFont(font)
        self.emp_code_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.emp_code_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_code_entry.setObjectName("emp_code_entry")
        self.full_name_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.full_name_entry.setGeometry(QtCore.QRect(530, 370, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.full_name_entry.setFont(font)
        self.full_name_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.full_name_entry.setText("")
        self.full_name_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.full_name_entry.setObjectName("full_name_entry")
        cps_generator_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(cps_generator_window)
        QtCore.QMetaObject.connectSlotsByName(cps_generator_window)

        # my code, outside pyqt5 designer
        self.generate_button.clicked.connect(self.generate)


    def retranslateUi(self, cps_generator_window):
        _translate = QtCore.QCoreApplication.translate
        cps_generator_window.setWindowTitle(_translate("cps_generator_window", "ECI Toolbox v2.00"))
        self.welcome_label.setText(_translate("cps_generator_window", "Generator kodów pracowniczych"))
        self.generate_button.setText(_translate("cps_generator_window", "Generuj"))
        self.send_to_printer_button.setText(_translate("cps_generator_window", "Drukuj"))
        self.emp_code_label.setText(_translate("cps_generator_window", "Kod pracownika:"))
        self.full_name_label.setText(_translate("cps_generator_window", "Imię i nazwisko:"))


    def goback(self):
        MainWindow.close()
        os.system("python main.py")


    def generate(self):
        with open("templates\\employee_code.prn") as f:
            input_file = f.read()
        with open(self.emp_code_entry.text() + ".prn", "w", encoding="utf-8") as wf:
            wf.write(Template(input_file).safe_substitute
                     (first=self.emp_code_entry.text(), second=self.full_name_entry.text()))
        try:
            shutil.move(os.getcwd() + "\\" + str(self.emp_code_entry.text()) + ".prn", desktop_path)
        except shutil.Error:
            # without asking and checking for int in emp_code_entry because it doesnt
            # matter for company needs - we also use this module for other purposes like generate a barcode with harness
            # number - like 1234567-A :)
            os.remove(desktop_path + str(self.emp_code_entry.text()) + ".prn")
            shutil.move(os.getcwd() + "\\" + str(self.emp_code_entry.text()) + ".prn", desktop_path)
        self.emp_code_entry.clear()
        self.full_name_entry.clear()
        final_path = desktop_path + "\\" + str(self.emp_code_entry.text()) + ".prn"
        return final_path

    def print_function(self):  # warning - hard-coded batch command for printing .prn file!
        try:
            final_path, printer_var = self.generate ()
        except TypeError:  # type error is raised when user try print label which doesn't have template -
            # FileNotFoundError was raised in generate() function so i don't put another error message here.
            return
        if os.system (f"COPY /B {final_path + printer_var} \\\EUPLUNIT206DT\\TSC_TC200"):  # check if printing done
            ctypes.windll.user32.MessageBoxW (0, 'Nie znaleziono drukarki.', "Wystąpił błąd", 0x10)
        time.sleep (2)
        os.remove (final_path + printer_var)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_cps_generator_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
