from flask import Flask, render_template, url_for, request, flash, g
from site_db import DB_query
import sqlite3, os

app = Flask(__name__)
app.config['SECRET_KEY'] = '0502ddaaedf75a5077746c5f370cd1711357b9a3'
Project = "Книжный магазин"
menu = [
    {"m_name": "Главная", "url": "index"},
    {"m_name": "О нас", "url": "about"},
    {"m_name": "Каталог", "url": "catalog"},
    {"m_name": "Обратная связь", "url": "contact"},
]
DATABASE = 'book.db'
DEBUG = True
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'book.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', title=f"{Project}: Главная", menu=menu)


@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    db = get_db()
    dbase = DB_query(db)
    ln_desc = 10
    if request.method == "POST":
        if len(request.form['description']) > ln_desc:
            res = dbase.add_book(request.form['name'], request.form['author'], request.form['description'],
                                 request.form['url'])
            if not res:
                flash("Ошибка добавления  книги", category="error")
            else:
                flash("Книга успешно добавлена", category="success")

    return render_template('add_book.html', menu=menu, title="Добавление новой книги", ln_desc=ln_desc)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title=f"{Project}: О нас", menu=menu)

@app.route("/book/<b_url>")
def show_book(b_url):
    db = get_db()
    dbase = DB_query(db)
    name, author, description, url = dbase.getbook(b_url)
    return render_template('book.html', menu=menu, title=f"Книга:{name}({author})", name=name, author=author, desc=description, url=url)

@app.route("/catalog")
def catalog():
    db = get_db()
    dbase = DB_query(db)
    print(url_for("catalog"))
    return render_template('catalog.html', title=f"{Project}: Каталог товаров", menu=menu, books=dbase.show_books())


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено", category='success')
        else:
            flash("Ошибка отпавки", category='error')
    return render_template('contact.html', title=f"{Project}: Обратная связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title=f"{Project}: Страница не найдена", menu=menu)

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html", title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
