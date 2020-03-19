from PyQt5.QtWidgets import QWidget, QApplication
from design import Ui_Form as Design
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        self.plainTextEdit.setPlainText("Название блюда\tКоличество\tСтоимость")
        a = 0
        if self.checkBox.isChecked():
            self.plainTextEdit.appendPlainText(f"Мак Фреш \t\t {self.spinBox.value()} \t {self.spinBox.value() * 149} руб.")
            a += self.spinBox.value() * 149
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText(f"Чизбургер \t\t {self.spinBox_2.value()} \t {self.spinBox_2.value() * 50} руб.")
            a += self.spinBox_2.value() * 50
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText(f"Роял \t\t {self.spinBox_3.value()} \t {self.spinBox_3.value() * 139} руб.")
            a += self.spinBox_3.value() * 139
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText(f"Соус Карри \t\t {self.spinBox_4.value()} \t {self.spinBox_4.value() * 25} руб.")
            a += self.spinBox_4.value() * 25
        if self.checkBox_5.isChecked():
            self.plainTextEdit.appendPlainText(f"Чай черный \t\t {self.spinBox_5.value()} \t {self.spinBox_5.value() * 70} руб.")
            a += self.spinBox_5.value() * 70
        self.plainTextEdit.appendPlainText(f"Итого: {a} рублей")


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())