from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY']='0502ddaaedf75a5077746c5f370cd1711357b9a3'
Project = "Книжный магазин"
menu = [
    {"m_name": "Главная", "url":"index"},
    {"m_name": "О нас", "url":"about"},
    {"m_name": "Каталог", "url":"catalog"},
    {"m_name": "Обратная связь", "url":"contact"},
]

@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', title=f"{Project}: Главная", menu=menu)

@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title=f"{Project}: О нас", menu=menu)

@app.route("/catalog")
def catalog():
    print(url_for("catalog"))
    return render_template('catalog.html', title=f"{Project}: Каталог товаров", menu=menu)
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method=="POST":
        if len(request.form['username'])> 2:
            flash("Сообщение отправлено", category='success')
        else:
            flash("Ошибка отпавки", category='error')
    return render_template('contact.html', title=f"{Project}: Обратная связь", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title=f"{Project}: Страница не найдена", menu=menu)

if __name__=='__main__':
    app.run(debug=True)