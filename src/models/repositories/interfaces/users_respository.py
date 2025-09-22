from abc import ABC, abstractmethod
from src.models.entities.users import Users


# classe abastratada: não pode criar objetos dela, é utilizada como herança
class UsersRepositoryInteface(ABC):

    # assinaturas das funções da classe de UsersRepository
    # metodos abstratos como decoradores
    # -> a classe que recebe como herança tem que obrigariamente implementar os elementos insert_user e select_user
    @abstractmethod
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        pass

    # assinaturas das funções da classe de UsersRepository
    @abstractmethod
    def select_user(self, person_name: str) -> list[Users]:
        pass
