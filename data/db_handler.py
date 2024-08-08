import sqlite3


def login(name, passw, signal):
    con = sqlite3.connect('data/handler')
    cur = con.cursor()
    req = """
        SELECT *
        FROM users 
        WHERE login = ?
    """
    value = cur.execute(req, (name,)).fetchall()
    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте правильность ввода данных!')
    cur.close()
    con.close()


def register(name, passw, signal):
    con = sqlite3.connect('data/handler')
    cur = con.cursor()

    req = """
        SELECT * 
        FROM users
        WHERE login = ?
    """
    value = cur.execute(req, (name,)).fetchall()

    if value:
        signal.emit('Такой ник уже используется!')

    elif not value:
        req = """
            INSERT INTO users (login, password) VALUES (?, ?)
        """
        cur.execute(req, (name, passw))
        signal.emit('вы успешно зарегистрировались!')
        con.commit()

    cur.close()
    con.close()
