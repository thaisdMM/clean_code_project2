from src.models.repositories.interfaces.users_respository import UsersRepositoryInteface


class UserFinder:
    # inversão da depedência - D SOLID
    def __init__(self, user_repository: UsersRepositoryInteface):
        self.__users_repo = user_repository

    def find_by_person_name(self, person_name: str) -> dict:
        selected_users = self.__select_and_validate_user(person_name)
        return self.__format_response(selected_users)

    def __select_and_validate_user(self, person_name: str) -> list:
        selected_users = self.__users_repo.select_user(person_name)
        if not selected_users or len(selected_users) == 0:
            raise Exception("Usuário não encontrado!")

        return selected_users

    # selected_users: lista da entidade de users
    def __format_response(self, selected_users: list) -> dict:
        formatted_users = []
        for users in selected_users:
            formatted_users.append(
                {
                    "id": users.id,
                    "person_name": users.person_name,
                    "height": users.height,
                }
            )
            return {
                "Type": "Users",
                "count": len(formatted_users),
                "atributes": formatted_users,
            }
