from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

@bp_produto.route('/')
def listaProduto():
    return render_template('listaProduto.html'), 200

@bp_produto.route('/form')
def formProduto():
    return render_template('formProduto.html'), 200