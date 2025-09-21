# pytest aquivos com _test e funções com _test

import pytest
from .db_connection_handler import DbConnectionHandler


# teste de integridade da conexão com o banco de dados, não é teste unitario
# a linha abaixo(skip) é para pular o teste, se quiser fazer o teste,
# tem que comentar ou apagar a linha abaixo
@pytest.mark.skip(reason="Integrations with DB")
def test_db_connection_handler():
    db_conn_handler = DbConnectionHandler()

    assert db_conn_handler.session is None

    with db_conn_handler:
        assert db_conn_handler.session is not None


# testes que falham, só para conferir se estão mesmo funcionando
# # testar se session começa com um valor que não é None -> fail
# def test_db_connection_handler_not_none():
#     db_conn_handler = DbConnectionHandler()

#     assert db_conn_handler.session is not None

# def test_db_connection_handler_with_none():
#     db_conn_handler = DbConnectionHandler()

#     assert db_conn_handler.session is None

#     with db_conn_handler:
#         print(db_conn_handler.session)
#         assert db_conn_handler.session is None
