from .__rest import REST
from .__request import Request

class Backup(Request):
    _rest = REST["backup"]

    def get_file_backup_list(self):
        return self._do_request(self._rest["get_file_backup_list"])
    
    def get_mysql_backup_list(self):
        return self._do_request(self._rest["get_mysql_backup_list"])

    def get_file_list(self, backup_id: int, path: str="/"):
        params = {"backup_id": backup_id, "path": path}
        return self._do_request(self._rest["get_file_list"], params)

    def get_mysql_list(self, backup_id: int):
        params = {"backup_id": backup_id}
        return self._do_request(self._rest["get_mysql_list"], params)

    def restore_file(self, backup_id: int, paths: list):
        params = {"backup_id": backup_id, "paths": paths}
        return self._do_request(self._rest["restore_file"], params)

    def restore_mysql(self, backup_id: int, bases: list):
        params = {"backup_id": backup_id, "bases": bases}
        return self._do_request(self._rest["restore_mysql"], params)

    def download_file(self, backup_id: int, paths: list):
        params = {"backup_id": backup_id, "paths": paths}
        return self._do_request(self._rest["download_file"], params)

    def download_mysql(self, backup_id, bases):
        params = {"backup_id": backup_id, "bases": bases}
        return self._do_request(self._rest["download_mysql"], params)

    def get_log(self):
        return self._do_request(self._rest["get_log"])
