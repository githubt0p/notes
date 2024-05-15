from view.MainWindow import MainWindow as Wn
import sqlite3
from database.data.sql_scripts import note_sql_script_create_table

connection = sqlite3.connect('database.db')

note_sql_script_create_table()

if __name__ == '__main__':
    window = Wn(connection=connection)
    window.mainloop()

connection.close()
