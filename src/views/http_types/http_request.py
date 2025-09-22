# classe de entrada da view: sempre vai retonar essa classe para o main,
# para tirar as informações da requisição http das rotas
class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.body = body
        self.param = param
