import sqlite3
import sys

from db.hieroglyphs import *
from handler.db_connect import *
from PyQt5 import QtCore
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

# Заготовка передачи строки. Еще надо ее разложить на элеенты (столбцы конкретные взять)

def show_me_dictionary(): # Надо подставить значения из БД из одной строки поэлментно

    # query = ""
    # cursor.execute(query, ())
    i = 1 # this_row в if select_row_and_this_element(this_row, element):
    form.label_number.setText(f'{select_row_and_this_element(i, 0)}')

    form.label_hieroglyph.setText(f'{select_row_and_this_element(i, 1)}')

    form.label_pinyin.setText(f'{select_row_and_this_element(i, 2)}')

    form.label_translation.setText(f'{select_row_and_this_element(i, 3)}')

    form.label_phrase.setText(f'{select_row_and_this_element(i, 4)}')

    form.label_HSK.setText(f'{select_row_and_this_element(i, 5)}')

def end_all():
    sys.exit(app.exec_())




form.checkBox_show_hsk1.stateChanged.connect(btn_hsk1)
form.pushButton_start_all.clicked.connect(show_me_dictionary)
form.pushButton_end.clicked.connect(end_all)
app.exec_()
