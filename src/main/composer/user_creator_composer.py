from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_creator import UserCreator
from src.views.user_creator_view import UserCreatorView


def user_creator_composer():
    # A ordem de criação e injeção de dependências é crucial para garantir que cada classe receba os objetos de que precisa para funcionar corretamente.
    # fazer a chamada de baixo para cima(view até connection) ajuda, vendo qual é cada dependencia que é necessaria
    connection = DbConnectionHandler()
    model = UsersRepository(connection)
    controller = UserCreator(model)
    view = UserCreatorView(controller)

    return view
