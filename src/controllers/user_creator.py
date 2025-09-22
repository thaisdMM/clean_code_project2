from src.models.repositories.interfaces.users_respository import UsersRepositoryInteface


class UserCreator:
    # users_repository recebe a interface -> inversão da dependencia - D SOLID
    def __init__(self, users_repository: UsersRepositoryInteface):
        self.__user_repo = users_repository
