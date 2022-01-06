from flask import Flask
from waitress import serve
from flask import render_template, request, redirect
from flask import session, flash, url_for
import os
from values import *
from op_bd import *

app = Flask(__name__)
app.secret_key = 'chave'


@app.route('/')
def start():
    return render_template(
        'index.html',
        titulo='Loja',
        produtos=itens_values()
    )


@app.route('/estoque')
def estoque():
    if 'usuario_autenticado' not in session or session['usuario_autenticado'] == None:
        return redirect(url_for('login', prox=url_for('estoque')))
    return render_template(
        'lista.html',
        titulo='Controle de Estoque',
        produtos=itens_values()
    )


@app.route('/funcionarios')
def funcionarios():
    if 'usuario_autenticado' not in session or session['usuario_autenticado'] == None:
        return redirect(url_for('login', prox=url_for('funcionarios')))
    return render_template(
        'lista_funcionarios.html',
        titulo='Funcionários',
        funcionarios=funcionarios_values()
    )


@app.route('/cadastro')
def cadastro():
    if 'usuario_autenticado' not in session or session['usuario_autenticado'] == None:
        return redirect(url_for('login', prox=url_for('cadastro')))
    return render_template('cadastro.html', titulo='Cadastro')


@app.route('/cadastro_funcionario')
def cadastro_funcionario():
    if 'usuario_autenticado' not in session or session['usuario_autenticado'] == None:
        return redirect(url_for('login', prox=url_for('cadastro_funcionario')))
    return render_template('cadastro_funcionario.html', titulo='Cadastro Funcionário')


@app.route('/AdicionarNovo', methods=['POST', ])
def AdicionarNovo():

    codigo = request.form['codigo']
    descricao = request.form['descricao']
    tamanho = request.form['tamanho']
    preco = request.form['preco']
    item = {
        "codigo": codigo, "descricao": descricao,
        "tamanho": tamanho, "preco": preco
    }

    resp = insert_item(item)
    if resp:
        flash('Item Inserido!')
    else:
        flash('Erro ao inserir item!')

    return redirect(url_for('estoque'))


@app.route('/DeletarItem/<codigo>', methods=['GET', 'POST', ])
def DeletarItem(codigo):
    resp = delete_item(codigo)
    if resp:
        flash('Item Excluído!')
    else:
        flash('Erro ao excluir item!')

    return redirect(url_for('estoque'))


@app.route('/AdicionarFuncionario', methods=['POST', ])
def AdicionarFuncionario():

    cpf = request.form['cpf']
    nome = request.form['nome']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    login = request.form['login']
    senha = request.form['senha']

    item = {
        "cpf": cpf, "nome": nome,
        "telefone": telefone, "endereco": endereco,
        "login": login, "senha": senha
    }

    resp = insert_funcionario(item)
    if resp:
        flash('Funcionario Inserido!')
    else:
        flash('Erro ao inserir funcionario!')

    return redirect(url_for('funcionarios'))


@app.route('/DeletarFuncionario/<cpf>', methods=['GET', 'POST', ])
def DeletarFuncionario(cpf):
    resp = delete_funcionario(cpf)
    if resp:
        flash('Usuário Deletado!')
    else:
        flash('Erro ao deletar usuário!')

    return redirect(url_for('funcionarios'))


@app.route('/login')
def login():
    prox = request.args.get('prox')
    return render_template('login.html', prox=prox)


@app.route('/autenticacao', methods=['POST', ])
def autenticacao():
    login = users_in_db(request.form['user'])
    print("entrou")
    if login:
        users = user(request.form['user'])[0]
        if users['senha'] == request.form['senha']:
            session['usuario_autenticado'] = users['login']
            flash(users['nome'] + ' está autenticado!')
            nextPage = request.form['prox']
            return redirect(nextPage)
    else:
        flash('Erro')
        return redirect(url_for('login'))


@app.route('/deslogar')
def deslogar():
    session['usuario_autenticado'] = None
    flash('Não há usuários autenticados!')
    return redirect(url_for('start'))


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
