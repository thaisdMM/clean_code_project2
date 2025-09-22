import pytest
from src.models.entities.users import Users
from .user_finder import UserFinder


# Classe Mock -> criando dados ficticios para nao acessar o banco de dados
# interface
class UserRepositoryMock:
    def __init__(self):
        # coleta as informações para os testes
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [Users(id=123, person_name="moked_person", height=2.12)]


# teste unitário != do de integração
def test_find_person_by_name():
    person_name = "my_person_name"
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)

    response = user_finder.find_by_person_name(person_name)
    # print(response)
    # # output: {'Type': 'Users', 'count': 1, 'atributes': [{'id': 123, 'person_name': 'moked_person', 'height': 2.12}]}
    # print(user_repository.select_user_att)  # output: {'person_name': 'my_person_name'}
    assert user_repository.select_user_att["person_name"] == person_name
    assert isinstance(response, dict)
    assert response["Type"] == "Users"
    assert "atributes" in response
    assert isinstance(response["atributes"], list)


# teste do erro


class UserRepositoryMockWithError:
    def __init__(self):
        # coleta as informações para os testes
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []


def test_find_by_person_name_with_error():
    user_repository = UserRepositoryMockWithError()
    user_finder = UserFinder(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_finder.find_by_person_name("something")

    # print(exc_info) # output: <ExceptionInfo Exception('Usuário não encontrado!') tblen=3>
    assert str(exc_info.value) == "Usuário não encontrado!"
