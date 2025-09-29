from pydantic import BaseModel, constr, ValidationError
from src.validators.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def user_creator_validator(http_request: any) -> None:

    # Esta classe é definida localmente para agrupar as regras de validação do Pydantic. Serve para:
    #  Aumentar a legibilidade: Agrupar a lógica de validação e a definição de dados no mesmo lugar.
    # Limitar a visibilidade: Evitar que a definição de dados "vaze" para outras partes do código.
    class BodyData(BaseModel):
        person_name: constr(min_length=1)  # type: ignore
        age: int
        height: float

    try:
        BodyData(**http_request.body)

    except ValidationError as error:
        raise HttpUnprocessableEntityError(error.errors()) from error
