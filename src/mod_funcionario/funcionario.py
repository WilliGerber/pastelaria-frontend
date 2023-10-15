from flask import Blueprint, render_template

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

@bp_funcionario.route('/')
def listaFuncionario():
    return render_template('listaFuncionario.html'), 200

@bp_funcionario.route('/form')
def formFuncionario():
    return render_template('formFuncionario.html'), 200