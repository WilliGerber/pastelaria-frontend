from flask import Blueprint, render_template
import requests
from settings import HEADERS_API, ENDPOINT_CLIENTE


bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

# @bp_cliente.route('/')
# def listaCliente():
#     return render_template('listaCliente.html'), 200

@bp_cliente.route('/form')
def formCliente():
    return render_template('formCliente.html'), 200


@bp_cliente.route('/', methods=['GET', 'POST'])
def listaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers = HEADERS_API)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('listaCliente.html', result=result[0])
    except Exception as e:
        return render_template('listaCliente.html', msgErro=e.args[0])