from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionHandler:
    def __init__(self):
        # string de conexão
        self.__connection_string = "sqlite:///schema.db"
        self.__engine = self.__create_database_engine()
        self.session = None

    # motor de conexão
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        # bind: ligaçao com o motor de conexão e a session(conexão com o banco de dados)
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        # retornando todo o contexto dessa classe
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
