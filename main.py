from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton,\
QLineEdit, QTreeWidget,QHeaderView, QTreeWidgetItem
import time
import sys

import user_py.calculate
# import user_Cplus.calculate

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

        self.type_label = QLabel("Тип данных:")
        self.type_cb = QComboBox()
        self.type_cb.addItems(choose.types_by_language[self.language_cb.currentText()])

        self.language_cb.currentTextChanged.connect(self.on_language_changed)

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
        self.load()

    def on_language_changed(self, language):
        self.type_cb.clear()
        self.type_cb.addItems(choose.types_by_language[language])

    def active_button(self):
        if self.quantity_input.styleSheet() == "QLineEdit { background-color: white; }":
            self.calculate_button.setEnabled(True)
        else:
           self.calculate_button.setEnabled(False)

    def validate(self, text):
            input_field = self.sender()
            try:
                num = float(text)
                if num == int(num) and int(num) <= 200*10**6:
                    input_field.setStyleSheet("QLineEdit { background-color: white; }")
                    return 1
                else:
                    raise Exception
            except Exception:
                input_field.setStyleSheet("QLineEdit { background-color: rgb(255, 200, 200); }")

    def load(self):
        index_ADD = 8
        with open('results.txt', 'r', encoding = 'UTF-8') as file:
            for line in file:
                text = line.strip().split('  ')
                main = text[:index_ADD]
                item = QTreeWidgetItem(main)
                self.tree.addTopLevelItem(item)

                if 'ADD:' in text:
                    add_text = text[index_ADD+1:]
                    add_info = QTreeWidgetItem(add_text)
                    item.addChild(add_info)

                self.vbox.addWidget(self.tree)


    def calculate(self):
        if "Py" in self.language_cb.currentText():
            text = [str(i) for i in [self.quantity_input.text(), self.language_cb.currentText(),self.type_cb.currentText(), self.operation_cb.currentText(), self.generation_cb.currentText(), '---', '---', 'Ошибка']]
            try:
                info = user_py.calculate.result_time(method=self.generation_cb.currentText(), quantity=int(self.quantity_input.text()), operation=self.operation_cb.currentText(), type_data = self.type_cb.currentText())
                if info:
                    text[-1] = "Завершено"
                    if self.generation_cb.currentText() == 'переменные':
                        text[-2] =  str(info[1])
                    else:
                        text[-2] =  str(info[3])
                    text[-3] = str(info[0])
                    item = QTreeWidgetItem(text)
                    self.tree.addTopLevelItem(item)
                    #TODO название файла в переменную

                    if self.generation_cb.currentText() == 'массив':
                        add_text = ['Время генерации массива: ', str(info[1]), 'С учётом генерации:', str(info[1] + info[0])] #"Массив:", str(info[2])
                        add_info = QTreeWidgetItem(add_text)
                        item.addChild(add_info)

                        with open('results.txt', 'a', encoding = 'UTF-8') as file:
                            file.write('  '.join(i for i in text) +'  ADD:  ' + ' '.join(i for i in add_text) +'\n')
                    else:
                        with open('results.txt', 'a', encoding = 'UTF-8') as file:
                            file.write('  '.join(i for i in text)+'\n')


            except Exception as exp:
                text[-1] = str(exp)
                item = QTreeWidgetItem(text)
                self.tree.addTopLevelItem(item)

            self.vbox.addWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(1200, 600)
    ex.show()
    sys.exit(app.exec_())
