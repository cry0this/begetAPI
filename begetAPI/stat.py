from begetAPI import site
from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Stat(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["stat"]

    async def get_site_list_load(self) -> Answer:
        return await self._do_request(self._rest["get_site_list_load"])

    async def get_db_list_load(self) -> Answer:
        return await self._do_request(self._rest["get_db_list_load"])

    async def get_site_load(self, site_id: int) -> Answer:
        return await self._do_request(self._rest["get_site_load"], {
            "site_id": site_id
        })

    async def get_db_load(self, db_name: str) -> Answer:
        return await self._do_request(self._rest["get_db_load"], {
            "db_name": db_name
        })
