import json
import requests

from .__answer import Answer


class Request:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password

    def _do_request(self, url: str, params: dict=None) -> Answer:
        request_params = {"login": self._login, "passwd": self._password}
        if params is not None:
            request_params["input_format"] = "json"
            request_params["input_data"] = json.dumps(params, separators=(',',':'))
        result = requests.get(url, request_params)
        return Answer(result.text)
