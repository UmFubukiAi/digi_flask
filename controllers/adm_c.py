from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.adm import Adm
from utils import db

bp_adm = Blueprint('adm', __name__, template_folder='../templates')

@bp_adm.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        novo = Adm(nome, email, senha)
        db.session.add(novo)
        db.session.commit()
        flash('Adm criado com sucesso!')
        return redirect(url_for('index'))
    return render_template('create_adm.html')

@bp_adm.route('/recovery')
def recovery():
    adm = Adm.query.all()
    return render_template('recovery_adm.html', adm=adm)

@bp_adm.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    adm = Adm.query.get(id)
    if request.method == 'POST':
        adm.nome = request.form['nome']
        adm.email = request.form['email']
        if request.form['senha']:
            adm.senha = request.form['senha']
        db.session.commit()
        flash('Adm atualizado!')
        return redirect(url_for('adm.recovery'))
    return render_template('update_adm.html', adm=adm)

@bp_adm.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    adm = Adm.query.get(id)
    if request.method == 'POST':
        db.session.delete(adm)
        db.session.commit()
        flash('Adm excluído!')
        return redirect(url_for('adm.recovery'))
    return render_template('delete_adm.html', adm=adm)

@bp_adm.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        adm = Adm.query.filter_by(email=email, senha=senha).first()
        if adm:
            session['adm_id'] = adm.id
            session['adm_nome'] = adm.nome
            flash('Login realizado!')
            return redirect(url_for('adm.perfil'))
        flash('Credenciais inválidas')
    return render_template('login.html')

@bp_adm.route('/logout')
def logout():
    session.clear()
    flash('Logout efetuado')
    return redirect(url_for('adm.login'))

@bp_adm.route('/perfil')
def perfil():
    if 'adm_id' not in session:
        flash('Faça login primeiro')
        return redirect(url_for('adm.login'))
    adm = Adm.query.get(session['adm_id'])
    return render_template('perfil_adm.html', adm=adm)
