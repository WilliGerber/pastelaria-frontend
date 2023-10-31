from flask import Blueprint, render_template
import requests
from settings import HEADERS_API, ENDPOINT_FUNCIONARIO

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

# @bp_funcionario.route('/')
# def listaFuncionario():
#     return render_template('listaFuncionario.html'), 200

@bp_funcionario.route('/form')
def formFuncionario():
    return render_template('formFuncionario.html'), 200

@bp_funcionario.route('/', methods=['GET', 'POST'])
def listaFuncionario():
    response = requests.get(ENDPOINT_FUNCIONARIO, headers = HEADERS_API)
    result = response.json()
    if (response.status_code != 200):
        raise Exception(result[0])
    return render_template('listaFuncionario.html', result=result[0])
