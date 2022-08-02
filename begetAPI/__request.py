import aiohttp
import json
import requests

from typing import Coroutine, Union

from .__answer import Answer


class Request:
    def __init__(self, login: str, password: str, asynchronous: bool=False) -> None:
        self._login = login
        self._password = password
        self._asynchronous = asynchronous

    def _do_request(self, url: str, params: Union[dict, None] = None) -> Union[Answer, Coroutine]:
        request_params = {"login": self._login, "passwd": self._password}

        if params is not None:
            request_params["input_format"] = "json"
            request_params["input_data"] = json.dumps(params, separators=(',',':'))

        if self._asynchronous:
            return self._do_async_request(url, request_params)

        response = requests.get(url, request_params)
        return Answer(response.text)

    async def _do_async_request(self, url, params) -> Answer:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=params) as response:
                return Answer(await response.text())
