from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Backup(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["backup"]

    def get_file_backup_list(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_file_backup_list"])

    def get_mysql_backup_list(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_mysql_backup_list"])

    def get_file_list(self, backup_id: int, path: str="/") -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_file_list"], {
            "backup_id": backup_id,
            "path": path
        })

    def get_mysql_list(self, backup_id: int) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_mysql_list"], {
            "backup_id": backup_id
        })

    def restore_file(self, backup_id: int, paths: list) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["restore_file"], {
            "backup_id": backup_id,
            "paths": paths
        })

    def restore_mysql(self, backup_id: int, bases: list) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["restore_mysql"], {
            "backup_id": backup_id,
            "bases": bases
        })

    def download_file(self, backup_id: int, paths: list) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["download_file"], {
            "backup_id": backup_id,
            "paths": paths
        })

    def download_mysql(self, backup_id, bases) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["download_mysql"], {
            "backup_id": backup_id,
            "bases": bases
        })

    def get_log(self) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_log"])
