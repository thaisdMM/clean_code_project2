from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.entities.users import Users


class UsersRepository:
    # injeção de dependencia da conexao com o banco de dados
    def __init__(self, db_conn_handler: DbConnectionHandler):
        self.__db_conn_handler = db_conn_handler

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        with self.__db_conn_handler as database:
            try:
                # os parametros de Users() vão ser passados para os parametros desse metodo
                new_user = Users(person_name=person_name, age=age, height=height)
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                # rollback voltar ao estado anterior antes de levantar a exceção
                database.session.rollback()
                raise exception

    def select_user(self, person_name: str) -> list[Users]:
        with self.__db_conn_handler as database:
            users = (
                database.session.query(Users)
                .filter(Users.person_name == person_name)
                .all()
            )
            return users
