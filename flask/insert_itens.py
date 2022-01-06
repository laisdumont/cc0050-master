import sqlite3


itens = [
          {
            "codigo": "1234", "descricao": "Blusinha top",
            "tamanho": "G", "preco": 50.00
          },
          {
            "codigo": "1235", "descricao": "Camisa HP",
            "tamanho": "P", "preco": 69.90
          },
          {
            "codigo": "1236", "descricao": "Camisa Pokemon",
            "tamanho": "M", "preco": 79.90
          }

]

conn = sqlite3.connect('flask/sistema_loja.db')

cursor = conn.cursor()

for item in itens:
    cursor.execute("""
            INSERT INTO itens(codigo, descricao, tamanho, preco)
            VALUES (?, ?, ?, ?)
    """, (item['codigo'], item['descricao'], item['tamanho'], item['preco']))

print("Dados inseridos")

conn.commit()
conn.close()
