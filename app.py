from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reading'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# Fungsi untuk menampilkan halaman registrasi
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hash_password,))
        mysql.connection.commit()
        cur.close()
        
        session['name'] = name
        session['email'] = email
        return redirect(url_for("home"))


# Fungsi untuk logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("home"))


# Fungsi untuk menampilkan halaman login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            # Email ditemukan dalam database, lanjutkan dengan pengecekan password
            if bcrypt.checkpw(password, user['password'].encode('utf-8')):
                session['email'] = user['email']  # Simpan email pengguna dalam sesi
                return redirect(url_for('readinglog'))
            else:
                # Password salah
                flash('Invalid email or password', 'error')
                return redirect(url_for('login'))
        else:
            # Email tidak terdaftar
            flash('Email is not registered', 'error')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')



@app.route('/readinglog', methods=["GET", "POST"])
def readinglog():
    if 'email' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Books")
        books = cur.fetchall()
        cur.close()
        return render_template("readinglog.html", books=books, show_auth_links=True)
    else:
        if request.method == 'POST':
            # Ini adalah penanganan form login atau registrasi
            if request.form['action'] == 'login':
                # Penanganan login
                email = request.form['email']
                password = request.form['password'].encode('utf-8')
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                user = cur.fetchone()
                cur.close()
                if user and bcrypt.checkpw(password, user['password'].encode('utf-8')):
                    session['name'] = user['name']
                    session['email'] = user['email']
                    # Redirect ke halaman readinglog setelah login berhasil
                    return redirect(url_for('readinglog'))
                else:
                    # Gagal login, kembali ke halaman readinglog
                    return redirect(url_for('readinglog'))
            elif request.form['action'] == 'register':
                # Penanganan registrasi
                # Lakukan validasi dan tindakan yang sesuai
                # Misalnya, tambahkan data pengguna baru ke database
                pass
            else:
                return "Error: Unknown action"
        
        # Ambil data buku dari database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Books WHERE user_email = %s", (user_email,))
        books = cur.fetchall()
        cur.close()

        return render_template("readinglog.html", books=books, show_auth_links=False)

@app.route('/add_book', methods=["POST"])
def add_book():
    if 'email' in session:
        if request.method == 'POST':
            if 'title' in request.form and 'date' in request.form:
                title = request.form['title']
                date = request.form['date']

                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO Books (title, date) VALUES (%s, %s)", (title, date,))
                mysql.connection.commit()
                cur.close()

                return redirect(url_for('readinglog'))
            else:
                return "Error: Please fill out all fields"
    else:
        return redirect(url_for('login'))


@app.route('/')
def home():
    show_readinglog_link = True  # Menampilkan tautan "Add Book" di navbar
    show_auth_links = False  # Menyembunyikan tautan login dan registrasi di navbar
    return render_template("home.html", show_readinglog_link=show_readinglog_link, show_auth_links=show_auth_links)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/enrollment')
def enrollment():
    return render_template('enrollment.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



if __name__ == '__main__':
    app.secret_key = "012#!ApaAjaBoleh)(*^%"
    app.run(debug=True)
