from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Ftp(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["ftp"]

    def get_list(self) -> Answer:
        return self._do_request(self._rest["get_list"])

    def add(self, suffix: str, homedir: str, password: str) -> Answer:
        return self._do_request(self._rest["add"], {
            "suffix": suffix,
            "homedir": homedir,
            "password": password
        })

    def change_password(self, suffix: str, password: str) -> Answer:
        return self._do_request(self._rest["change_password"], {
            "suffix": suffix,
            "password": password
        })

    def delete(self, suffix: str) -> Answer:
        return self._do_request(self._rest["delete"], {
            "suffix": suffix
        })
