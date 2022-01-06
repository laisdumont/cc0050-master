import sqlite3


def insert_item(item):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO itens(codigo, descricao, tamanho, preco)
                VALUES (?, ?, ?, ?)
        """, (item['codigo'], item['descricao'], item['tamanho'], item['preco']))

        conn.commit()

    except:
        conn.close()
        return False
    
    else:
        conn.close()
        return True


def insert_funcionario(fun):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        cursor = conn.cursor()

        cursor.execute("""
                    INSERT INTO funcionarios(cpf, nome, telefone, endereco, login, senha)
                    VALUES (?, ?, ?, ?, ?, ?)
            """, (fun['cpf'], fun['nome'], fun['telefone'], fun['endereco'], fun['login'], fun['senha']))
    
        conn.commit()

    except:
        conn.close()
        return False
    
    else:
        conn.close()
        return True


def users_in_db(login):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        query = f"""
                    SELECT nome, login, senha
                    FROM funcionarios WHERE login = '{login}';
            """
        cursor = conn.execute(query)
        employers_dict = [
                            {'nome': row[0], 'login': row[1], 'senha': row[2]}
                            for row in cursor.fetchall()
                        ]

        a = {'funcionarios': employers_dict}

    except:
        conn.close()
        return False

    else:
        if len(a['funcionarios']) == 0:
            return False
        else:
            print(a['funcionarios'])
            return True


def user(login):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        query = f"""
                    SELECT nome, login, senha
                    FROM funcionarios WHERE login = '{login}';
            """
        cursor = conn.execute(query)
        employers_dict = [
                            {'nome': row[0], 'login': row[1], 'senha': row[2]}
                            for row in cursor.fetchall()
                        ]

        a = {'funcionarios': employers_dict}

    except:
        conn.close()
    else:
        return a['funcionarios']


def select_itens():
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        query = """
                    SELECT codigo, descricao, tamanho, preco
                    FROM itens ORDER BY descricao;
            """
        cursor = conn.execute(query)
        employers_dict = [
                            {'codigo': linha[0], 'descricao': linha[1], 'tamanho': linha[2], 'preco': linha[3]}
                            for linha in cursor.fetchall()
                        ]

    except:
        conn.close()

    else:
        return ({'itens': employers_dict})


def select_funcionario():
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        query = """
                    SELECT cpf, nome, telefone, endereco
                    FROM funcionarios ORDER BY nome;
            """
        cursor = conn.execute(query)
        employers_dict = [
                            {'cpf': row[0], 'nome': row[1], 'telefone': row[2], 'endereco': row[3]}
                            for row in cursor.fetchall()
                        ]

    except:
        conn.close()

    else:
        return ({'funcionarios': employers_dict})


def delete_item(codigo):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        cursor = conn.cursor()

        cursor.execute(f"""
                            DELETE FROM itens WHERE codigo = '{codigo}'
                        """)
        conn.commit()

    except:
        conn.close()
        return False
    
    else:
        conn.close()
        return True


def delete_funcionario(cpf):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')
        cursor = conn.cursor()

        cursor.execute(f"""
                DELETE FROM funcionarios WHERE cpf = '{cpf}'
        """)
        
        conn.commit()
    except:
        conn.close()
        return False

    else:
        conn.close()
        return True


def update_funcionario(campo, valor, cpf):
    try:
        conn = sqlite3.connect('flask/sistema_loja.db')

        cursor = conn.cursor()
        cursor.execute(f"""
                UPDATE funcionarios
                SET {campo} = '{valor}'
                WHERE cpf = '{cpf}'
        """)

        conn.commit()

    except:
        conn.close()
        return False
    
    else:
        conn.close()
        return True
