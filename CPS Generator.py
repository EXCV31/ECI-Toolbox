from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from string import Template
import os
import shutil
from limits import *
import ctypes
import time

desktop_path = os.path.join (os.path.join (os.path.join (os.environ['USERPROFILE']), 'Desktop\\'))


class Ui_cps_generator_window (object):
    def setupUi(self, cps_generator_window):
        cps_generator_window.setObjectName ("cps_generator_window")
        cps_generator_window.resize (1018, 681)
        cps_generator_window.setWindowIcon (QIcon ('transfer.png'))
        self.centralwidget = QtWidgets.QWidget (cps_generator_window)
        self.centralwidget.setObjectName ("centralwidget")
        self.generator_label = QtWidgets.QLabel (self.centralwidget)
        self.generator_label.setGeometry (QtCore.QRect (50, 30, 240, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (20)
        self.generator_label.setFont (font)
        self.generator_label.setObjectName ("generator_label")
        self.comboBox = QtWidgets.QComboBox (self.centralwidget)
        self.comboBox.setGeometry (QtCore.QRect (50, 80, 191, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (12)
        self.comboBox.setFont (font)
        self.comboBox.setEditable (False)
        self.comboBox.setFrame (True)
        self.comboBox.setObjectName ("comboBox")
        self.comboBox.addItem ("")
        self.comboBox.addItem ("")
        self.comboBox.addItem ("")
        self.width_label = QtWidgets.QLabel (self.centralwidget)
        self.width_label.setGeometry (QtCore.QRect (310, 30, 190, 34))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.width_label.setFont (font)
        self.width_label.setObjectName ("width_label")
        self.height_label = QtWidgets.QLabel (self.centralwidget)
        self.height_label.setGeometry (QtCore.QRect (555, 30, 190, 31))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.height_label.setFont (font)
        self.height_label.setObjectName ("height_label")
        self.gap_label = QtWidgets.QLabel (self.centralwidget)
        self.gap_label.setGeometry (QtCore.QRect (780, 30, 160, 31))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.gap_label.setFont (font)
        self.gap_label.setObjectName ("gap_label")
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.generate_button = QtWidgets.QPushButton (self.centralwidget)
        self.generate_button.setGeometry (QtCore.QRect (830, 560, 151, 51))
        self.generate_button.setObjectName ("generate_button")
        self.send_to_printer_button = QtWidgets.QPushButton (self.centralwidget)
        self.send_to_printer_button.setGeometry (QtCore.QRect (620, 560, 151, 51))
        self.send_to_printer_button.setObjectName ("send_to_printer_button")
        self.first_line_label = QtWidgets.QLabel (self.centralwidget)
        self.first_line_label.setGeometry (QtCore.QRect (270, 210, 161, 34))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.first_line_label.setFont (font)
        self.first_line_label.setObjectName ("first_line_label")
        self.second_line_label = QtWidgets.QLabel (self.centralwidget)
        self.second_line_label.setGeometry (QtCore.QRect (270, 290, 141, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.second_line_label.setFont (font)
        self.second_line_label.setObjectName ("second_line_label")
        self.third_line_label = QtWidgets.QLabel (self.centralwidget)
        self.third_line_label.setGeometry (QtCore.QRect (270, 370, 131, 31))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.third_line_label.setFont (font)
        self.third_line_label.setObjectName ("third_line_label")
        self.first_entry = QtWidgets.QLineEdit (self.centralwidget)
        self.first_entry.setGeometry (QtCore.QRect (530, 210, 431, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.first_entry.setFont (font)
        self.first_entry.setFocusPolicy (QtCore.Qt.ClickFocus)
        self.first_entry.setAlignment (QtCore.Qt.AlignCenter)
        self.first_entry.setObjectName ("first_entry")
        self.second_entry = QtWidgets.QLineEdit (self.centralwidget)
        self.second_entry.setGeometry (QtCore.QRect (530, 290, 431, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.second_entry.setFont (font)
        self.second_entry.setFocusPolicy (QtCore.Qt.ClickFocus)
        self.second_entry.setText ("")
        self.second_entry.setAlignment (QtCore.Qt.AlignCenter)
        self.second_entry.setObjectName ("second_entry")
        self.third_entry = QtWidgets.QLineEdit (self.centralwidget)
        self.third_entry.setGeometry (QtCore.QRect (530, 370, 431, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.third_entry.setFont (font)
        self.third_entry.setCursor (QtGui.QCursor (QtCore.Qt.IBeamCursor))
        self.third_entry.setFocusPolicy (QtCore.Qt.ClickFocus)
        self.third_entry.setAlignment (QtCore.Qt.AlignCenter)
        self.third_entry.setClearButtonEnabled (False)
        self.third_entry.setObjectName ("third_entry")
        self.limits_label = QtWidgets.QLabel (self.centralwidget)
        self.limits_label.setGeometry (QtCore.QRect (310, 100, 190, 34))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.limits_label.setFont (font)
        self.limits_label.setObjectName ("limits_label")
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.harness_id_entry = QtWidgets.QLineEdit (self.centralwidget)
        self.harness_id_entry.setGeometry (QtCore.QRect (770, 100, 191, 41))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.harness_id_entry.setFont (font)
        self.harness_id_entry.setFocusPolicy (QtCore.Qt.ClickFocus)
        self.harness_id_entry.setAlignment (QtCore.Qt.AlignCenter)
        self.harness_id_entry.setObjectName ("harness_id_entry")
        self.harness_id_label = QtWidgets.QLabel (self.centralwidget)
        self.harness_id_label.setGeometry (QtCore.QRect (590, 100, 161, 34))
        font = QtGui.QFont ()
        font.setFamily ("Source Sans Pro Light")
        font.setPointSize (16)
        self.harness_id_label.setFont (font)
        self.harness_id_label.setObjectName ("harness_id_label")
        self.generator_label.raise_ ()
        self.width_label.raise_ ()
        self.height_label.raise_ ()
        self.gap_label.raise_ ()
        self.generate_button.raise_ ()
        self.send_to_printer_button.raise_ ()
        self.first_line_label.raise_ ()
        self.second_line_label.raise_ ()
        self.third_line_label.raise_ ()
        self.first_entry.raise_ ()
        self.second_entry.raise_ ()
        self.third_entry.raise_ ()
        self.limits_label.raise_ ()
        self.comboBox.raise_ ()
        self.harness_id_entry.raise_ ()
        self.harness_id_label.raise_ ()
        cps_generator_window.setCentralWidget (self.centralwidget)
        self.retranslateUi (cps_generator_window)
        self.comboBox.setCurrentIndex (0)
        QtCore.QMetaObject.connectSlotsByName (cps_generator_window)

        # my code, outside pyqt5 designer
        self.comboBox.currentIndexChanged.connect (self.combobox_changed)
        self.generate_button.clicked.connect (self.generate)
        self.send_to_printer_button.clicked.connect (self.print_function)

    def retranslateUi(self, cps_generator_window):
        _translate = QtCore.QCoreApplication.translate
        cps_generator_window.setWindowTitle (_translate ("cps_generator_window", "ECI Toolbox v2.00"))
        self.generator_label.setText (_translate ("cps_generator_window", "Generator CPS"))
        self.comboBox.setPlaceholderText (_translate ("cps_generator_window", "Wybierz projekt..."))
        self.comboBox.setItemText (0, _translate ("cps_generator_window", "SampleProject"))
        self.comboBox.setItemText (1, _translate ("cps_generator_window", "AnotherSampleProject"))
        self.comboBox.setItemText (2, _translate ("cps_generator_window", "AndAnotherSampleProject"))
        self.width_label.setText (_translate ("cps_generator_window", "Szerokość: 30mm"))
        self.height_label.setText (_translate ("cps_generator_window", "Wysokość: 10mm"))
        self.gap_label.setText (_translate ("cps_generator_window", "Przerwa: 3mm"))
        self.generate_button.setText (_translate ("cps_generator_window", "Generuj"))
        self.send_to_printer_button.setText (_translate ("cps_generator_window", "Drukuj"))
        self.first_line_label.setText (_translate ("cps_generator_window", "Pierwsza linia:"))
        self.second_line_label.setText (_translate ("cps_generator_window", "Druga linia:"))
        self.third_line_label.setText (_translate ("cps_generator_window", "Trzecia linia:"))
        self.limits_label.setText (_translate ("cps_generator_window", "Limity: 8/16/16"))
        self.harness_id_label.setText (_translate ("cps_generator_window", "Numer Wiązki:"))

    def goback(self):
        MainWindow.close ()
        os.system ("python main.py")

    def combobox_changed(self):
        if self.comboBox.currentText () == "SampleProject":
            limit1 = SampleProject_limit1
            limit2 = SampleProject_limit2
            limit3 = SampleProject_limit3
            height = SampleProject_label_height
            width = SampleProject_label_width
            gap = SampleProject_label_gap
        if self.comboBox.currentText () == "AnotherSampleProject":
            limit1 = AnotherSampleProject_limit1
            limit2 = AnotherSampleProject_limit2
            limit3 = AnotherSampleProject_limit3
            height = AnotherSampleProject_label_height
            width = AnotherSampleProject_label_width
            gap = AnotherSampleProject_label_gap
        if self.comboBox.currentText () == "AndAnotherSampleProject":
            limit1 = AndAnotherSampleProject_limit1
            limit2 = AndAnotherSampleProject_limit2
            limit3 = AndAnotherSampleProject_limit3
            height = AndAnotherSampleProject_label_height
            width = AndAnotherSampleProject_label_width
            gap = AndAnotherSampleProject_label_gap
        self.limits_label.setText (f"Limity: {limit1} / {limit2} / {limit3}")
        self.height_label.setText (f"Wysokość: {height}")
        self.width_label.setText (f"Szerokość: {width}")
        self.gap_label.setText (f"Przerwa: {gap}")

    def clean(self):
        self.third_entry.clear ()
        self.second_entry.clear ()
        self.first_entry.clear ()

    def generate(self):
        if self.third_entry.text () != "":
            example = f"templates\\{self.comboBox.currentText ()}3.prn"
        elif self.second_entry.text () != "":
            example = f"templates\\{self.comboBox.currentText ()}2.prn"
        elif self.first_entry.text () != "":
            example = f"templates\\{self.comboBox.currentText ()}1.prn"
        try:
            with open (example) as f:
                input_file = f.read ()
        except FileNotFoundError:
            ctypes.windll.user32.MessageBoxW (0, 'Brak wzorca dla danego projektu.', "Wystąpił błąd", 0x10)
            self.clean ()
            return
        with open (self.first_entry.text () + ".prn", "w", encoding="utf-8") as wf:
            wf.write (Template (input_file).safe_substitute
                      (first=self.first_entry.text (), second=self.second_entry.text (),
                       third=self.third_entry.text ()))

        final_path = desktop_path
        if self.harness_id_entry != "":
            destination_folder = desktop_path + str (self.harness_id_entry.text ()) + "\\"
            os.makedirs (destination_folder, exist_ok=True)
            final_path = destination_folder

        if os.path.isfile (final_path + str (self.first_entry.text () + ".prn")):
            question = ctypes.windll.user32.MessageBoxW (0, "Plik istnieje. Podmienić?", "Wystąpił błąd", 4)
            if question == 6:
                os.remove (final_path + str (self.first_entry.text () + ".prn"))
                shutil.move (os.getcwd () + "\\" + str (self.first_entry.text ()) + ".prn", final_path)
                return
            elif question == 7:
                return
        shutil.move (os.getcwd () + "\\" + str (self.first_entry.text ()) + ".prn", final_path)
        printer_var = self.first_entry.text () + ".prn"
        self.clean ()
        return final_path, printer_var

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

    app = QtWidgets.QApplication (sys.argv)
    MainWindow = QtWidgets.QMainWindow ()
    ui = Ui_cps_generator_window ()
    ui.setupUi (MainWindow)
    MainWindow.show ()
    sys.exit (app.exec_ ())
