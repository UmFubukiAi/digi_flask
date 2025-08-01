from flask import render_template, request, redirect, flash, Blueprint
from models.usuario import Usuario
from utils import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('recovery.html', usuarios = usuarios)

@bp_usuarios.route('/create')
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
        return redirect(url_for('.recovery'))
    
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
        return redirect(url_for('.update', id=id))
    db.session.add(usuario)
    db.session.commit()
    flash("Dados atualizados!")
    return redirect(url_for('.recovery', id=id)) 