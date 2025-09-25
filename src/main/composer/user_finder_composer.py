from src.views.user_finder_view import UserFinderView
from src.controllers.user_finder import UserFinder
from src.models.repositories.users_repository import UsersRepository
from src.models.connection.db_connection_handler import DbConnectionHandler


def user_finder_composer():

    # A ordem de criação e injeção de dependências é crucial para garantir que cada classe receba os objetos de que precisa para funcionar corretamente.
    # fazer a chamada de baixo para cima(view até connection) ajuda, vendo qual é cada dependencia que é necessaria
    connection = DbConnectionHandler()
    model = UsersRepository(connection)
    controller = UserFinder(model)
    view = UserFinderView(controller)

    return view
