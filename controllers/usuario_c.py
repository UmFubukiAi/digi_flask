from flask import render_template, request, redirect, flash, Blueprint, url_for
from models.usuario import Usuario
from models.adm import Adm
from utils import db
from datetime import date

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')
bp_adm = Blueprint("adm", __name__, template_folder='templates')

@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('recovery.html', usuarios = usuarios)

@bp_usuarios.route('/create', methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('create.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        usuario = Usuario(nome, email, senha)
        db.session.add(usuario)
        db.session.commit()
        flash('Dados cadastrados com sucesso!')
        return redirect(url_for('usuarios.recovery'))
    
@bp_usuarios.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if id and request.method=='GET':
        usuario = Usuario.query.get(id)
        return render_template('update.html', usuario = usuario)
    if request.method=='POST':
        usuario = Usuario.query.get(id)
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
    if (request.form.get('senha') and request.form.get('senha') == request.form.get('csenha')):
        usuario.senha = request.form.get('senha')
    else:
        flash('Senhas não são iguais')
        return redirect(url_for('usuarios.update', id=id))
    db.session.add(usuario)
    db.session.commit()
    flash("Dados atualizados!")
    return redirect(url_for('usuarios.recovery', id=id)) 

@bp_usuarios.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    if id==0:
        flash('É preciso definir um usuário para ser excluído')
        return redirect(url_for('usuarios.recovery'))
    if request.method == 'GET':
        usuario = Usuario.query.get(id)
        return render_template('delete.html', usuario = usuario)
    if request.method == 'POST':
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário excluído com sucesso')
        return redirect(url_for('usuarios.recovery'))
    
@bp_adm.route('/recovery')
def recovery():
    adm = Adm.query.all()
    return render_template('recovery.html', adm = adm)

@bp_adm.route('/create', methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('create.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        adm = Adm(nome, email, senha)
        db.session.add(adm)
        db.session.commit()
        flash('Dados cadastrados com sucesso!')
        return redirect(url_for('adm.recovery'))
    
@bp_adm.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if id and request.method=='GET':
        adm = Adm.query.get(id)
        return render_template('update.html', adm = adm)
    if request.method=='POST':
        adm = Adm.query.get(id)
        adm.nome = request.form.get('nome')
        adm.email = request.form.get('email')
    if (request.form.get('senha') and request.form.get('senha') == request.form.get('csenha')):
        adm.senha = request.form.get('senha')
    else:
        flash('Senhas não são iguais')
        return redirect(url_for('adm.update', id=id))
    db.session.add(adm)
    db.session.commit()
    flash("Dados atualizados!")
    return redirect(url_for('adm.recovery', id=id)) 

@bp_adm.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    if id==0:
        flash('É preciso definir um adm para ser excluído')
        return redirect(url_for('adm.recovery'))
    if request.method == 'GET':
        adm = Adm.query.get(id)
        return render_template('delete.html', adm = adm)
    if request.method == 'POST':
        adm = Adm.query.get(id)
        db.session.delete(adm)
        db.session.commit()
        flash('Adm excluído com sucesso')
        return redirect(url_for('adm.recovery'))
    
@bp_usuarios.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash('Login realizado com sucesso!')
            return redirect(url_for('usuarios.recovery'))
        else:
            flash('Email ou senha inválidos!')
            return redirect(request.url)
    return render_template('login.html')

@bp_usuarios.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da conta')
    return redirect(url_for('usuarios.login'))

@bp_usuarios.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar o perfil')
        return redirect(url_for('usuarios.login'))
    
    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('usuarios/perfil.html', usuario=usuario)