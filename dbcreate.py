import sqlite3

def db_create():
    db = sqlite3.connect('database_users.sql')
    command = db.cursor()
    command.execute("""CREATE TABLE IF NOT EXISTS Users(
        id int auto_increment primary key,
        NAME varchar,
        UID varchar UNIQUE,
        un varchar
        )""")
    db.commit()
    command.close()
    db.close ()

def db_add():
    pass