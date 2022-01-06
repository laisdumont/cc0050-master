import sqlite3


funciorarios = [
                  {
                    "cpf": "711273623", "nome": "Maria Eduarda",
                    "telefone": "27368192", "endereco": "Jardinhas",
                    "login": "mariazinha", "senha": "1234"
                  },
                  {
                    "cpf": "71167673", "nome": "Lais Dumont",
                    "telefone": "27368434", "endereco": "Santanas",
                    "login": "laisinha", "senha": "1235"
                  },
                  {
                    "cpf": "711273323", "nome": "Joan Derson",
                    "telefone": "27368324", "endereco": "Juazeiras",
                    "login": "joazinho", "senha": "1236"
                  }
]

conn = sqlite3.connect('flask/sistema_loja.db')

cursor = conn.cursor()

for fun in funciorarios:
    cursor.execute("""
            INSERT INTO funcionarios(cpf, nome, telefone, endereco, login, senha)
            VALUES (?, ?, ?, ?, ?, ?)
    """, (fun['cpf'], fun['nome'], fun['telefone'], fun['endereco'], fun['login'], fun['senha']))

print("Dados inseridos")

conn.commit()
conn.close()
