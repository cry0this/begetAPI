from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Backup(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["backup"]

    async def get_file_backup_list(self) -> Answer:
        return await self._do_request(self._rest["get_file_backup_list"])
    
    async def get_mysql_backup_list(self) -> Answer:
        return await self._do_request(self._rest["get_mysql_backup_list"])

    async def get_file_list(self, backup_id: int, path: str="/") -> Answer:
        return await self._do_request(self._rest["get_file_list"], {
            "backup_id": backup_id,
            "path": path
        })

    async def get_mysql_list(self, backup_id: int) -> Answer:
        return await self._do_request(self._rest["get_mysql_list"], {
            "backup_id": backup_id
        })

    async def restore_file(self, backup_id: int, paths: list) -> Answer:
        return await self._do_request(self._rest["restore_file"], {
            "backup_id": backup_id,
            "paths": paths
        })

    async def restore_mysql(self, backup_id: int, bases: list) -> Answer:
        return await self._do_request(self._rest["restore_mysql"], {
            "backup_id": backup_id,
            "bases": bases
        })

    async def download_file(self, backup_id: int, paths: list) -> Answer:
        return await self._do_request(self._rest["download_file"], {
            "backup_id": backup_id,
            "paths": paths
        })

    async def download_mysql(self, backup_id, bases) -> Answer:
        return await self._do_request(self._rest["download_mysql"], {
            "backup_id": backup_id,
            "bases": bases
        })

    async def get_log(self) -> Answer:
        return await self._do_request(self._rest["get_log"])
