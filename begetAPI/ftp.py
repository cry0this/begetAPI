from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Ftp(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["ftp"]

    def get_list(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_list"])

    def add(self, suffix: str, homedir: str, password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["add"], {
            "suffix": suffix,
            "homedir": homedir,
            "password": password
        })

    def change_password(self, suffix: str, password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["change_password"], {
            "suffix": suffix,
            "password": password
        })

    def delete(self, suffix: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["delete"], {
            "suffix": suffix
        })
