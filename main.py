import sqlite3
from db.hieroglyphs import *
from handler.users_login import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

From, Window = uic.loadUiType("views/cadr25_step2.ui")

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()

def create_main_table_for_show():
    hsk_db = sqlite3.connect('hsk_base.db')
    cursor = hsk_db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS main_table_for_show('
                   'number INTEGER, '
                   'hieroglyph TEXT, '
                   'pinyin TEXT, '
                   'translation TEXT, '
                   'phrase TEXT, hsk TEXT'
                   ')')

def insert_hsk_into_main_table():
    hsk_db = sqlite3.connect('hsk_base.db')
    cursor = hsk_db.cursor()
    print(hsk[0][1])
    for i in range(0, len(hsk)):
        cursor.execute('INSERT INTO main_table_for_show VALUES(?,?,?,?,?,?)', (
                        hsk[i][0], hsk[i][1], hsk[i][2], hsk[i][3], hsk[i][4], hsk[i][5]))
        hsk_db.commit()

# insert_hsk_into_main_table()
# create_main_table_for_show()
hsk_db = sqlite3.connect('hsk_base.db')
cursor = hsk_db.cursor()
cursor.execute("SELECT * FROM main_table_for_show WHERE hsk = 'HSK2'")
rez = cursor.fetchall()

# Определил, сколько я набрал по выборке строк
coumt_num = cursor.execute("SELECT COUNT(*) FROM main_table_for_show WHERE hsk = 'HSK2'").fetchall()
rezult = coumt_num[0][0] # Получил числовое значение, например 150
print(rezult)
for i in range(0, rezult):
    print(rez[i][1])



class Dictionary():
    __slots_ = ['number', 'hieroglyph', 'pinyin', 'translation', 'phrase', 'hsk']

    def __init__(self, number, hieroglyph, pinyin, translation, phrase, hsk):
        self.__number = number
        self.__hieroglyph = hieroglyph
        self.__pinyin = pinyin
        self.__translation = translation
        self.__phrase = phrase
        self.__hsk = hsk

    def one_dicionary(self):
        pass

app.exec_()
