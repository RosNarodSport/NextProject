import sqlite3
import sys

from db.hieroglyphs import *
from handler.db_connect import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from handler.users_login import cur

From, Window = uic.loadUiType("views/cadr25_step2.ui")

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()


def btn_hsk1():
    if form.checkBox_show_hsk1.isChecked() == True:
        print('метка hsk1 выставлена')


i = 100


def show_me_dictionary():
    form.label_number.setText(f'{select_row_and_this_element(i, 0)}')

    form.label_hieroglyph.setText(f'{select_row_and_this_element(i, 1)}')

    form.label_pinyin.setText(f'{select_row_and_this_element(i, 2)}')

    form.label_translation.setText(f'{select_row_and_this_element(i, 3)}')

    form.label_phrase.setText(f'{select_row_and_this_element(i, 4)}')

    form.label_HSK.setText(f'{select_row_and_this_element(i, 5)}')


def end_all():
    sys.exit(app.exec_())


def horizontalSlider_size_Value():
    hieroglyph_size = form.horizontalSlider_size.value()
    print(hieroglyph_size)
    if hieroglyph_size > 6 and hieroglyph_size < 50:
        form.label_hieroglyph.setFont(QFont('Arial', hieroglyph_size))
        form.label_for_horizontalSlider_size.setFont(QFont('Arial', hieroglyph_size))


form.checkBox_show_hsk1.stateChanged.connect(btn_hsk1)
form.pushButton_start_all.clicked.connect(show_me_dictionary)
form.pushButton_end.clicked.connect(end_all)

# Размер иероглифа
form.horizontalSlider_size.valueChanged.connect(horizontalSlider_size_Value)





# Комплект кода для авторизации
#
#
# base_line_edit = [form.lineEdit_user_name, form.lineEdit_user_password]
#
# # Проверка правильности ввода в поля логин и пароль
# def check_input(function):
#     print('Работает кнопка pushButton_login')
#
#     def wrapper():
#         for line_edit in base_line_edit:
#             if len(line_edit.text()) == 0:
#                 return
#             function()
#         return wrapper
#
# @check_input
# def authorization(function):
#
#     user_name = form.lineEdit_user_name.text()
#     user_password = form.lineEdit_user_password.text()
#     check_db.thr_login(user_name, user_password)
#
# @check_input
# def registration(function):
#     print('Работает кнопка pushButton_sign_up')
#     user_name = form.lineEdit_user_name.text()
#     user_password = form.lineEdit_user_password.text()
#     check_db.thr_login(user_name, user_password)
#
#
# global value
# # Обраотчик сигналов
# def signal_handler():
#     QtWidgets.QMessageBox.about('Оповещение', value)
#
# class CheckThread():
#     mysignal = QtCore.pyqtSignal(str)
#
#     def thr_login(self, user_name, user_password):
#         login(user_name, user_password, self.mysignal)
#
#     def thr_register(self, user_name, user_password):
#         register(user_name, user_password, self.mysignal)
#
#
# def login(user_name, user_password, signal):
#     con = sqlite3.connect('db/users.db')
#     cur = con.cursor()
#
#     # Проверка, есть ли такой пользователь
#     query = 'SELECT * FROM users WHERE user_name = ?'
#     cur.execute(query, (login,))
#     value = cur.fetchall()
#
#     if value != [] and value[0][2] == user_password:
#         signal.emit('Успешная авторищация')
#     else:
#         signal.emit('Проверьте правильность ввода пароляя')
#     cur.close()
#     con.close()
#
#
# def register():
#     pass
#
#
# check_db = CheckThread() # Создаем экземпляр класса одного модуля
# # check_db.mysignal.connect(signal_handler) # Обработчик сигнала
#
#
# # def check_db():
# #     pass
# #
# #
# # def CheckThread():
# #     pass
#
# # Комплекс регистрации польователя
# form.pushButton_login.clicked.connect(check_input)
# # form.pushButton_sign_up.clicked.connect(registration)

app.exec_()
