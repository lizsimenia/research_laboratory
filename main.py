from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton,\
QLineEdit, QTreeWidget,QHeaderView, QTreeWidgetItem
import time
import sys

import user_py.calculate
import choose

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Research...")

    def initUI(self):
        self.language_label = QLabel('Язык программирования:')
        self.language_cb = QComboBox()
        self.language_cb.addItems(choose.languages)

        #TODO типы данных зависят от яп
        self.type_label = QLabel("Тип данных:")
        self.type_cb = QComboBox()
        self.type_cb.addItems(choose.type)

        self.operation_label = QLabel('Операция:')
        self.operation_cb = QComboBox()
        self.operation_cb.addItems(choose.operations)

        self.generation_label = QLabel('Метод генерации чисел:')
        self.generation_cb = QComboBox()
        self.generation_cb.addItems(choose.generation_methods)

        self.quantity_label = QLabel('Количество чисел:')
        self.quantity_input = QLineEdit()
        self.quantity_input.setStyleSheet("QLineEdit { background-color: rgb(255, 200, 200); }")
        self.quantity_input.textChanged.connect(self.validate)
        self.quantity_input.textChanged.connect(self.active_button)

        self.calculate_button = QPushButton('Рассчитать')
        self.calculate_button.setEnabled(False)
        self.calculate_button.clicked.connect(self.calculate)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(choose.headers)
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.language_label)
        self.vbox.addWidget(self.language_cb)
        self.vbox.addWidget(self.type_label)
        self.vbox.addWidget(self.type_cb)
        self.vbox.addWidget(self.operation_label)
        self.vbox.addWidget(self.operation_cb)
        self.vbox.addWidget(self.generation_label)
        self.vbox.addWidget(self.generation_cb)
        self.vbox.addWidget(self.quantity_label)
        self.vbox.addWidget(self.quantity_input)
        self.vbox.addWidget(self.calculate_button)
        self.vbox.addWidget(self.tree)

        self.setLayout(self.vbox)

    def active_button(self):
        if self.quantity_input.styleSheet() == "QLineEdit { background-color: white; }":
            self.calculate_button.setEnabled(True)

    def validate(self, text):
            input_field = self.sender()
            try:
                num = float(text)
                if num == int(num):
                    input_field.setStyleSheet("QLineEdit { background-color: white; }")
                    return 1
                else:
                    raise Exception
            except Exception:
                input_field.setStyleSheet("QLineEdit { background-color: rgb(255, 200, 200); }")

    def calculate(self):
        num = '0'
        #TODO нумерация
        if "Py" in self.language_cb.currentText():
            text = [str(i) for i in [self.quantity_input.text(), self.language_cb.currentText(),self.type_cb.currentText(), self.operation_cb.currentText(), self.generation_cb.currentText(), '---', 'Ошибка']]
            try:
                info = user_py.calculate.result_time(method=self.generation_cb.currentText(), quantity=int(self.quantity_input.text()), operation=self.operation_cb.currentText(), type_data = self.type_cb.currentText())
                if info:
                    text[-1] = "Завершено"
                    text[-2] = str(info[0])
                    item = QTreeWidgetItem(text)
                    self.tree.addTopLevelItem(item)
                    #TODO название файла в переменную
                    with open('results.txt', 'a', encoding = 'UTF-8') as file:
                        file.write(' '.join(i for i in text))

                    if self.generation_cb.currentText() == 'массив':
                        add_text = ['Время генерации массива: ', str(info[1]), 'С учётом генерации:', str(info[1] + info[0])]
                        add_info = QTreeWidgetItem(add_text)
                        item.addChild(add_info)
                        with open('results.txt', 'a', encoding = 'UTF-8') as file:
                            file.write(' ADD:' + ' '.join(i for i in add_text) +'\n')


            except Exception:
                item = QTreeWidgetItem(text)
                self.tree.addTopLevelItem(item)

            self.vbox.addWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(600, 600)
    ex.show()
    sys.exit(app.exec_())
