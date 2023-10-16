from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

@bp_cliente.route('/')
def listaCliente():
    return render_template('listaCliente.html'), 200

@bp_cliente.route('/form')
def formCliente():
    return render_template('formCliente.html'), 200