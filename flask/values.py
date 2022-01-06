from op_bd import *

def itens_values():

    class Itens:
        def __init__(self, codigo, descricao, tamanho, preco):
            self.codigo = codigo
            self.descricao = descricao
            self.tamanho = tamanho
            self.preco = preco
    
    dictionary = select_itens()
    lista = []
    for i in dictionary['itens']:
        p = Itens(i['codigo'], i['descricao'], i['tamanho'], i['preco'])
        lista.append(p)

    return lista

def funcionarios_values():

    class Users:
        def __init__(self, cpf, nome, telefone, endereco):
            self.cpf = cpf
            self.nome = nome
            self.telefone = telefone
            self.endereco = endereco

    dictionary = select_funcionario()
    lista = []
    for i in dictionary['funcionarios']:
        p = Users(i['cpf'], i['nome'], i['telefone'], i['endereco'])
        lista.append(p)

    return lista

def user_auth():
    class User:
        def __init__(self, login, nome, senha):
            self.login = login
            self.nome = nome
            self.senha = senha

    dictionary = users()
    d = {}

    for i in dictionary['funcionarios']:
        user = User(i['login'], i['nome'], i['senha'])
        d.update({user.senha: user})
        user = 0

    return d
# user_auth()
