from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Dns(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["dns"]

    def get_data(self, fqdn: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_data"], {
            "fqdn": fqdn
        })

    def change_records(self, fqdn: str, records: dict) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["change_records"], {
            "fqdn": fqdn,
            "records": records
        })
