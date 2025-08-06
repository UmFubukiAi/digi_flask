from flask import render_template, request, redirect, flash, Blueprint, url_for, session
from models.usuario import Usuario
from utils import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder='../templates')

@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('recovery.html', usuarios = usuarios)

@bp_usuarios.route('/create', methods=['GET','POST'])
def create():
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        novo = Usuario(nome, email, senha)
        db.session.add(novo)
        db.session.commit()
        flash('Dados cadastrados com sucesso!')
        return redirect(url_for('usuarios.recovery'))
    return render_template('create.html')
    
@bp_usuarios.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    usuario = Usuario.query.get(id)
    if request.method=='POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        if request.form['senha']:
            usuario.senha = request.form['senha']
        db.session.commit()
        flash("Dados atualizados!")
        return redirect(url_for('usuarios.recovery'))
    return render_template('update.html', usuario = usuario)

@bp_usuarios.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário excluído com sucesso')
        return redirect(url_for('usuarios.recovery'))
    return render_template('delete.html', usuario = usuario)

@bp_usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash('Login realizado!')
            return redirect(url_for('usuarios.perfil'))
        flash('Credenciais inválidas')
    return render_template('login.html')

@bp_usuarios.route('/logout')
def logout():
    session.clear()
    flash('Logout efetuado')
    return redirect(url_for('usuarios.login'))

@bp_usuarios.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        flash('Faça login primeiro')
        return redirect(url_for('usuarios.login'))
    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('perfil.html', usuario=usuario)