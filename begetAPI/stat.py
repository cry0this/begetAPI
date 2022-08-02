from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Stat(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["stat"]

    def get_site_list_load(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_site_list_load"])

    def get_db_list_load(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_db_list_load"])

    def get_site_load(self, site_id: int) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_site_load"], {
            "site_id": site_id
        })

    def get_db_load(self, db_name: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_db_load"], {
            "db_name": db_name
        })
