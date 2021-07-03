from begetAPI import site
from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class User(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["user"]

    def get_account_info(self) -> Answer:
        return self._do_request(self._rest["get_account_info"])

    def toggle_ssh(self, status: bool, ftp_login: str=None) -> Answer:
        return self._do_request(self._rest["toggle_ssh"], {
            "status": status,
            "ftplogin": ftp_login
        })
