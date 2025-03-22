import sqlite3

class Database:
    def __init__(self, db_name="Sistema.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            ConfPassword TEXT NOT NULL,
            Pix TEXT NOT NULL
        )             
        """)
        self.conn.commit()

    def insert_user(self, username, email, password, conf_password,pix):
        if password != conf_password:
            raise ValueError("As senhas não coincidem.")
        self.cursor.execute("INSERT INTO users (Username, Email, Password, ConfPassword,Pix) VALUES (?, ?, ?, ?, ?)", 
                            (username, email, password, conf_password,pix))
        self.conn.commit()

        def verify_login(self, username, password):
            self.db.cursor.execute("SELECT * FROM users WHERE Username=? AND Password=?", (username, password))
            return self.db.cursor.fetchone() is not None

    def close(self):
        self.conn.close()
