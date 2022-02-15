import sqlite3
import sys
import datetime

from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from handler.db_connect import select_row_and_this_element

From, Window = uic.loadUiType("views/cadr25_step2.ui")

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()


def btn_hsk1():
    if form.checkBox_show_hsk1.isChecked() == True:
        print('метка hsk1 выставлена')


i = 100 # Тестовый параметр, с какого иероглифа начяать показ


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


def user_logged():
    try:
        rezult_l = form.lineEdit_user_name.text()
        rezult_p = form.lineEdit_user_password.text()
        base = sqlite3.connect('hsk_base.db')
        cur = base.cursor()
        query_login = "SELECT * FROM users WHERE user_name = ?"
        cur.execute(query_login, (rezult_l,))
        rezult_login = cur.fetchall()
        if rezult_login != [] and rezult_login[0][2] != rezult_p:
            form.label_info_for_user.setText("Введены\nнекорректные\nданные!")
        else:
            # Обновляю дату последнего обращения к программе
            form.label_info_for_user.setText("<span style='color: #008000;'>Успешный <br>вход</span>")
            form.label_user_name.setText(f'Вы вошли\nпод НИКом: {rezult_login[0][1]}')
            form.label_user_level.setText(f'Ваш уровень: {rezult_login[0][8]}')
            form.label_hsk_group.setText(f'{rezult_login[0][6]}')
            form.label_speed_show.setText(f'{rezult_login[0][4]} секунд')
            form.label_label_color_scheme_label.setText(
                f"<span style='color: {rezult_login[0][5]}' >Цветовая схема</span>")
            form.label_color_scheme.setText(f"<span style='color: {rezult_login[0][5]}' >{rezult_login[0][5]}</span>")
            form.label_show_new_start_point_2.setText(f'С номера -> {rezult_login[0][7]}')
            form.label_num_hieroglyphs_in_show.setText(f'Показ по {rezult_login[0][10]} шт.')
            form.label_hieroglyph_size.setText(f'{rezult_login[0][3]}')
            form.label_last_date.setText(f'{rezult_login[0][13]}')
    except:
        form.label_info_for_user.setText("<span style='color: #f00;'>Ошибка <br>ввода</span>")


def user_registration():
    print('Попытка регистрации')


# Комплекс регистрации польователя
form.pushButton_login.clicked.connect(user_logged)
form.pushButton_sign_up.clicked.connect(user_registration)

app.exec_()
