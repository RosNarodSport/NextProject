import sqlite3

from db.hieroglyphs import hsk

hsk_db = sqlite3.connect('hsk_base.db')
cursor = hsk_db.cursor()
def create_main_table_for_show():
    cursor.execute('CREATE TABLE IF NOT EXISTS main_table_for_show('
                   'number INTEGER, '
                   'hieroglyph TEXT, '
                   'pinyin TEXT, '
                   'translation TEXT, '
                   'phrase TEXT, hsk TEXT'
                   ')')


def insert_hsk_into_main_table():
    print(hsk[0][1])
    for i in range(0, len(hsk)):
        cursor.execute('INSERT INTO main_table_for_show VALUES(?,?,?,?,?,?)', (
            hsk[i][0], hsk[i][1], hsk[i][2], hsk[i][3], hsk[i][4], hsk[i][5]))
        hsk_db.commit()


# insert_hsk_into_main_table()
# create_main_table_for_show()

def secelction_hsk_group(hsk_group):
    cursor.execute("SELECT * FROM main_table_for_show WHERE hsk = ?", (hsk_group,))
    rez = cursor.fetchall()
    return rez


def get_number(hsk_group):
    coumt_num = cursor.execute("SELECT COUNT(*) FROM main_table_for_show WHERE hsk = ?", (hsk_group,)).fetchall()
    rezult = coumt_num[0][0]  # Получил числовое значение размера группы hsk, например 150
    return rezult


def print_my_hsk_group(hsk_group):
    for i in range(0, get_number(hsk_group)):
        print(secelction_hsk_group(hsk_group)[i][1])

def select_row(this_row): # Пробегаю по строкам. Работает
    query = "SELECT * FROM main_table_for_show WHERE number = ?"
    selected_row = cursor.execute(query, (this_row,)).fetchall()
    return selected_row


def select_row_and_this_element(this_row, element): # Надо вытащить элемент статьи (строки) конкретный
    raw = select_row(this_row)
    num = raw[0][0]
    # print('num: --->', num)
    this_element = ['number', 'hieroglyph', 'pinyin', 'translation', 'phrase', 'hsk']
    # print('this_element[element] ---> ', this_element[element])
    query_raw = f"SELECT {this_element[element]} FROM main_table_for_show WHERE number = ?"

    selected_row = cursor.execute(query_raw, (num, )).fetchall()
    print(selected_row[0][0])

    return selected_row[0][0]



if __name__ == "__main__":
    i = 1
    select_row_and_this_element(i, 0)
    select_row_and_this_element(i, 1)
    select_row_and_this_element(i, 2)
    select_row_and_this_element(i, 3)
    select_row_and_this_element(i, 4)
    select_row_and_this_element(i, 5)
