from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ctypes
from string import Template
import shutil
desktop_path = os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\'))

class Ui_multiple_labels_window(object):
    def setupUi(self, multiple_labels_window):
        multiple_labels_window.setObjectName("multiple_labels_window")
        multiple_labels_window.resize(1018, 681)
        self.centralwidget = QtWidgets.QWidget(multiple_labels_window)
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
        self.beginning_label = QtWidgets.QLabel(self.centralwidget)
        self.beginning_label.setGeometry(QtCore.QRect(240, 210, 231, 34))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.beginning_label.setFont(font)
        self.beginning_label.setObjectName("beginning_label")
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(240, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("full_name_label")
        self.beginning_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.beginning_entry.setGeometry(QtCore.QRect(530, 210, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.beginning_entry.setFont(font)
        self.beginning_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.beginning_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.beginning_entry.setObjectName("beginning_entry")
        self.amount_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_entry.setGeometry(QtCore.QRect(530, 370, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(16)
        self.amount_entry.setFont(font)
        self.amount_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.amount_entry.setText("")
        self.amount_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_entry.setObjectName("amount_entry")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        multiple_labels_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(multiple_labels_window)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(multiple_labels_window)

        # my code, outside pyqt5 designer
        self.generate_button.clicked.connect(self.generate)
        self.counter = 1


    def retranslateUi(self, cps_generator_window):
        _translate = QtCore.QCoreApplication.translate
        cps_generator_window.setWindowTitle(_translate("cps_generator_window", "ECI Toolbox v2.00"))
        self.welcome_label.setText(_translate("cps_generator_window", "Generator wielu etykiet na raz"))
        self.generate_button.setText(_translate("cps_generator_window", "Generuj"))
        self.beginning_label.setText(_translate("cps_generator_window", "Początek np. \"CRP\":"))
        self.amount_label.setText(_translate("cps_generator_window", "Ilość:"))
        self.comboBox.setPlaceholderText(_translate("cps_generator_window", "Wybierz projekt..."))
        self.comboBox.setItemText(0, _translate("cps_generator_window", "SampleProject"))
        self.comboBox.setItemText(1, _translate("cps_generator_window", "AndAnotherSampleProject"))
        self.comboBox.setItemText(2, _translate("cps_generator_window", "AnotherSampleProject"))


    def generate(self):
        example = f"templates\\{self.comboBox.currentText()}_multiple.prn"

        if self.beginning_entry.text() == "":
            ctypes.windll.user32.MessageBoxW(0, 'Nie wypełniono pola nr 1', "Wystąpił błąd", 0x10)
            return
        if self.amount_entry.text() == "":
            ctypes.windll.user32.MessageBoxW(0, 'Nie wypełniono pola nr 2', "Wystąpił błąd", 0x10)
            return
        try:
            int(self.amount_entry.text())
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, "Pole nr 2 powinno zawierać liczbę.", "Wystąpił błąd", 0x10)
        try:
            os.makedirs(desktop_path + "Wygenerowane CPS - " + self.beginning_entry.text() + "\\")
            save_path = desktop_path + "Wygenerowane CPS - " + self.beginning_entry.text() + "\\"
        except OSError:
            ctypes.windll.user32.MessageBoxW(0, f'Folder docelowy "Wygenerowane CPS - {self.beginning_entry.text()}" na'
                                                f' pulpicie nie jest pusty. '
                                                f'Skasuj folder i spróbuj ponownie.', "Wystąpił błąd", 0x10)
            return
        while self.counter -1 != int(self.amount_entry.text()):
            with open(example) as f:
                input_file = f.read()
            with open(self.beginning_entry.text() + str(self.counter) + ".prn", "w", encoding="utf-8") as wf:

                wf.write(Template(input_file).safe_substitute
                         (first=self.beginning_entry.text(), second=str(self.counter)))
            shutil.move(os.getcwd() + "\\" + self.beginning_entry.text() + str(self.counter) + ".prn", save_path)
            self.counter += 1

        ctypes.windll.user32.MessageBoxW(0, f'Wygenerowano {self.counter -1} etykiet, znajdziesz je w folderze '
                                            f'"Wygenerowane CPS - {self.beginning_entry.text()}" na pulpicie.',
                                            "Informacja", 0x40)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_multiple_labels_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
