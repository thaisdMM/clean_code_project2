import pytest
from .user_creator import UserCreator


# Classe Mock -> criando dados ficticios para nao acessar o banco de dados
class UserRepositoryMock:
    def __init__(self):
        # coleta as informçõs para os testes
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        self.insert_user_att["person_name"] = person_name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height


# teste unitário != do de integração
def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    person_name = "my_person_name"
    age = 33
    height = 1.69

    response = user_creator.insert_new_user(person_name, age, height)
    # print(response)
    # print(user_repository.select_user_att) # output: {'my_person_name': 'my_person_name'}
    assert user_repository.select_user_att["person_name"] == person_name
    assert user_repository.insert_user_att["age"] == age

    assert isinstance(response, dict)
    assert "Type" in response
    assert response["count"] == 1
    assert response["message"] == "Usuario cadastrado com sucesso!"


class UserRepositoryMockWithError:
    def __init__(self):
        # coleta as informçõs para os testes
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [1, 2, 3]


def test_inset_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UserCreator(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("something", 33, 1.90)

    # print(exc_info.value) # output: test_inset_new_user_with_error Usuário já cadastrado.
    assert str(exc_info.value) == "Usuario ja cadastrado."


# # só para conferir se o teste do erro estava mesmos funcionando
# def test_inset_new_user_with_error():
#     user_repository = UserRepositoryMock()
#     user_creator = UserCreator(user_repository)

#     with pytest.raises(Exception) as exc_info:
#         user_creator.insert_new_user("something", 33, 1.90)
# # output: Failed: DID NOT RAISE <class 'Exception'>
