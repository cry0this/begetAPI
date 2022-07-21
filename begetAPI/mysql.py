from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Mysql(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["mysql"]

    async def get_list(self) -> Answer:
        return await self._do_request(self._rest["get_list"])

    async def add_db(self, suffix: str, password: str) -> Answer:
        return await self._do_request(self._rest["add_db"], {
            "suffix": suffix,
            "password": password
        })

    async def add_access(self, suffix: str, access: str, password: str) -> Answer:
        return await self._do_request(self._rest["add_access"], {
            "suffix": suffix,
            "access": access,
            "password": password
        })

    async def drop_db(self, suffix: str) -> Answer:
        return await self._do_request(self._rest["drop_db"], {
            "suffix": suffix
        })

    async def drop_access(self, suffix: str, access: str) -> Answer:
        return await self._do_request(self._rest["drop_access"], {
            "suffix": suffix,
            "access": access
        })

    async def change_access_password(self, suffix: str, access: str, password: str) -> Answer:
        return await self._do_request(self._rest["change_access_password"], {
            "suffix": suffix,
            "access": access,
            "password": password
        })
