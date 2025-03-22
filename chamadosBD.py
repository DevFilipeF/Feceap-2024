import sqlite3

def create_table():
    try:
        conn = sqlite3.connect("chamados.db")  
        c = conn.cursor()
        # Cria a tabela `reciclagem` se não existir
        c.execute("""
        CREATE TABLE IF NOT EXISTS reciclagem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            local TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

# Chame a função `create_table` no início do programa
create_table()