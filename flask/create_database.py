import sqlite3

conn = sqlite3.connect('flask/sistema_loja.db')

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE funcionarios(
          cpf TEXT NOT NULL PRIMARY KEY,
          nome TEXT NOT NULL,
          telefone TEXT NOT NULL,
          endereco TEXT NOT NULL,
          login TEXT NOT NULL UNIQUE,
          senha TEXT NOT NULL
        );
""")

cursor.execute("""
        CREATE TABLE itens(
          codigo TEXT NOT NULL PRIMARY KEY,
          descricao TEXT NOT NULL,
          tamanho TEXT NOT NULL,
          preco FLOAT NOT NULL
        );
""")

print("Tabelas criadas!")

conn.close()
