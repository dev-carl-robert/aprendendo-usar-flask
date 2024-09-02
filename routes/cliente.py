from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

"""

    - /clientes/ (GET) - listar os clientes
    - /clientes/ (Post) inserir o cliente no servidor
    - /clientes/new (GET) - renderiza um formulario para criar um cliente
    - /clientes/<id> (GET) - obter dados de um cliente
    - /clientes/<id>/edit (GET) - renderiza um formulario para editar um cliente
    - /clientes/<id>/update (Put) - atualizar os dados de um cliente
    - /clientes/<id>/delete (Delete) - deleta o registro do cliente

"""

@cliente_route.route("/")
def lista_cliente():
    pass

@cliente_route.route("/<int:cliente_id>")
def obter_cliente(cliente_id) :
    print(cliente_id)
    pass