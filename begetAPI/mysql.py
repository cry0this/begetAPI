from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Mysql(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["mysql"]

    def get_list(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_list"])

    def add_db(self, suffix: str, password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["add_db"], {
            "suffix": suffix,
            "password": password
        })

    def add_access(self, suffix: str, access: str, password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["add_access"], {
            "suffix": suffix,
            "access": access,
            "password": password
        })

    def drop_db(self, suffix: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["drop_db"], {
            "suffix": suffix
        })

    def drop_access(self, suffix: str, access: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["drop_access"], {
            "suffix": suffix,
            "access": access
        })

    def change_access_password(self, suffix: str, access: str, password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["change_access_password"], {
            "suffix": suffix,
            "access": access,
            "password": password
        })
