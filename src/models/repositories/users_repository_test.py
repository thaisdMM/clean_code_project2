import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from .users_repository import UsersRepository


# teste de integração
@pytest.mark.skip(reason="Insert in DB")
def test_user_repository():
    db_conn = DbConnectionHandler()
    users_repo = UsersRepository(db_conn)

    person_name = "Nome de teste"
    age = 44
    height = 1.70

    users_repo.insert_user(person_name, age, height)
    users = users_repo.select_user(person_name)

    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height
