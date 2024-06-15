from flask import url_for
import math,time, re,sqlite3

class DB_query:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_book(self, name, author, desc, url):
        try:
            self.__cur.execute("select count() as 'count' FROM book WHERE url like ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                add_error = "Книга с таким URL уже существует"
                print(add_error)
                return False
            base = url_for('static', filename='images')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          r"\g<tag>" + base + r"/\g<url>>", desc)
            tm = math.floor(time.time())
            self.__cur.execute("Insert INTO book VALUES(NULL,?,?,?,?)", (name, author, desc, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка БД " + str(e))
            return False
        return True

    def show_books(self):
        sql = "SELECT id, name,author, description, url FROM book ORDER BY name"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статей из БД: " + str(e))
        return []


    def getbook(self, alias):

        try:
            self.__cur.execute(f"select name, author,description,url from book where url='{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения книги из БД " + str(e))
            return False, False