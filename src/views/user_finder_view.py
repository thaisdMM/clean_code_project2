from src.controllers.interfaces.user_finder import UserFinderInterface
from src.validators.errors.error_handler import handler_errors
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserFinderView:
    def __init__(self, controller: UserFinderInterface):
        self.__controller = controller

    def handler_find_by_person_name(self, request: HttpRequest) -> HttpResponse:
        try:
            person_name = request.param["person_name"]

            response = self.__controller.find_by_person_name(person_name)

            return HttpResponse(status_code=200, body=response)

        except Exception as exception:
            return handler_errors(exception)
