import sqlite3

functions_txt = ["1.Добавить новое слово",
"2.Показать все слова",
"3.Удалить слово",
"4.Изменить слово",
"5.Изменить перевод слова",
"6.Выйти из словаря"
]

def append_word():
    new_word = input("Введите новое слово:").lower()
    new_word_translate = input("Введите перевод:").lower()
    new_word1 = (new_word,new_word_translate)
    cur.execute("INSERT INTO words VALUES(?, ?);",new_word1 )
    conn.commit()
    print("Слово успешно добавлено!")

def show_all():
    cur.execute("SELECT * FROM words")
    for row in cur.fetchall():
        print(f"Слово:{row[0]} | Перевод:{row[1]}")

def delete_word():
    deleting_word = input("Введите слово,которое хотите удалить:")
    cur.execute("SELECT * FROM words")
    for row in cur.fetchall():
        if deleting_word == row[0]:
            cur.execute("DELETE FROM words WHERE word = ?",(deleting_word,))
            conn.commit()
            print("Слово успешно удалено!")
        else:
            print("Такого слова нет в словаре")

def change_word():
    old_word = input("Введите слово которое, хотите изменить:")
    cur.execute("SELECT * FROM words")
    for row in cur.fetchall():
        if old_word == row[0]:
            new_word2 = input("Введите новое слово:").lower()
            cur.execute("UPDATE words SET word = ? WHERE word = ?",\
                        (new_word2,old_word,))
            conn.commit()
            print("Слово успешно изменено!")
            break
    else:
        print("Такого слова нет в словаре")
            

def change_translate():
    old_translate = input("Введите перевод, хотите изменить:")
    cur.execute("SELECT * FROM words")
    for row in cur.fetchall():
        if old_translate == row[1]:
            new_translate = input("Введите новый перевод:")
            cur.execute("UPDATE words SET translate = ? WHERE translate = ?",\
                        (new_translate,old_translate,))
            conn.commit()
            print("Перевод успешно добавлен!")
            break
    else:
        print("Такого перевода нет в словаре")
            


for row in functions_txt:
    print(row)

conn = sqlite3.connect("words.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS words(
    word TEXT,
    translate TEXT
);""")
conn.commit()
while True:
    answer = input("Введите номер функции которую хотите выполнить:")
    if answer == "1":
        append_word()
    if answer == "2":
        show_all()
    if answer == "3":
        delete_word()
    if answer == "4":
        change_word()
    if answer == "5":
        change_translate()
    if answer == "6":
        print("Работа завершена...")
        break
    

