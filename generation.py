import user_py.calculate
import main

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton,\
QLineEdit, QTreeWidget,QHeaderView, QTreeWidgetItem
import time
import sys

app = QApplication(sys.argv)
for i in range(200*10**6, 10**6, -10*10**6):
    try:
        main_app = main.App()
        if main_app.layout() is None:
            main_app.initUI()

        main_app.language_cb.setCurrentText('Python')
        main_app.type_cb.setCurrentText('int')
        main_app.operation_cb.setCurrentText('+')
        main_app.generation_cb.setCurrentText('переменные')
        main_app.quantity_input.setText(str(i))
        main_app.calculate()

        main_app.operation_cb.setCurrentText('-')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('/')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('*')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('log')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('sqrt')
        main_app.calculate()

        main_app.type_cb.setCurrentText('float')
        main_app.operation_cb.setCurrentText('+')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('-')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('/')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('*')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('log')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('sqrt')
        main_app.calculate()


        main_app.language_cb.setCurrentText('Python')
        # main_app.type_cb.setCurrentText('int')
        main_app.operation_cb.setCurrentText('+')
        main_app.generation_cb.setCurrentText('переменные')
        main_app.quantity_input.setText(str(i))
        # main_app.calculate()

        main_app.operation_cb.setCurrentText('-')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('/')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('*')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('log')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('sqrt')
        main_app.calculate()


        main_app.type_cb.setCurrentText('float')
        main_app.operation_cb.setCurrentText('+')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('-')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('/')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('*')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('log')
        main_app.calculate()

        main_app.operation_cb.setCurrentText('sqrt')
        main_app.calculate()


    except Exception as exp:
        print(f'ERROR : {str(exp)}')
        break
else:
    print(f"Done")
app.exec_()
