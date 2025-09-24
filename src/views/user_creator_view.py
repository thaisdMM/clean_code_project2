from src.controllers.interfaces.user_creator import UserCreatorInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserCreatorView:
    def __init__(self, controller: UserCreatorInterface):
        self.__controller = controller

    def handler_insert_new_user(self, request: HttpRequest) -> HttpResponse:
        try:
            person_name = request.body["person_name"]
            age = request.body["age"]
            height = request.body["height"]

            response = self.__controller.insert_new_user(person_name, age, height)
            return HttpResponse(status_code=200, body=response)
        except Exception as exception:
            return HttpResponse(body={"error": str(exception)}, status_code=500)
