from PyQt5.QtSql import *

def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()

        # Create Tabel
        sql = '''CREATE TABLE phonebook(
            Id INTEGER NOT NULL PRIMARY KEY,
            Nama VARCHAR(25),
            Nohp VARCHAR (15)
        )'''
        query.exec_(sql)
        if(query.exec_):
            print('Berhasil Create Tabel')

    else:
        Print('ERROR: ' + db.lastError().text())
connectdb()