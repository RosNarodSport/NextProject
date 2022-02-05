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

select_row_and_this_element(0)
select_row_and_this_element(1)
select_row_and_this_element(2)
select_row_and_this_element(3)
select_row_and_this_element(4)
select_row_and_this_element(5)

def show_me_dictionary(): # Надо подставить значения из БД из одной строки поэлментно

    # query = ""
    # cursor.execute(query, ())

    form.label_number.setText('number')

    form.label_hieroglyph.setText('hieroglyph')

    form.label_pinyin.setText('pinyin')

    form.label_translation.setText('translation')

    form.label_phrase.setText('phrase')

    form.label_HSK.setText('hsk')


hsk_group = 'HSK1'
this_element = ['number', 'hieroglyph', 'pinyin', 'translation', 'phrase', 'hsk']

rrr = select_row(1)
print('--------------')
print(rrr)

# select_row_and_this_element(rrr, this_element[0])

# print_my_hsk_group(hsk_group)

def end_all():
    sys.exit(app.exec_())




form.checkBox_show_hsk1.stateChanged.connect(btn_hsk1)
form.pushButton_start_all.clicked.connect(show_me_dictionary)
form.pushButton_end.clicked.connect(end_all)
app.exec_()
