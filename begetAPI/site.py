from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Site(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["site"]

    def get_list(self) -> Answer:
        return self._do_request(self._rest["get_list"])

    def add(self, name: str) -> Answer:
        return self._do_request(self._rest["add"], {
            "name": name
        })

    def delete(self, id: int) -> Answer:
        return self._do_request(self._rest["delete"], {
            "id": id
        })

    def link_domain(self, domain_id: int, site_id: int) -> Answer:
        return self._do_request(self._rest["link_domain"], {
            "domain_id": domain_id,
            "site_id": site_id
        })

    def unlink_domain(self, domain_id: int) -> Answer:
        return self._do_request(self._rest["unlink_domain"], {
            "domain_id": domain_id
        })

    def freeze(self, id: int, excluded_paths: list) -> Answer:
        return self._do_request(self._rest["freeze"], {
            "id": id,
            "excludedPaths": excluded_paths
        })

    def unfreeze(self, id: int) -> Answer:
        return self._do_request(self._rest["unfreeze"], {
            "id": id
        })

    def is_site_frozen(self, site_id: int) -> Answer:
        return self._do_request(self._rest["is_site_frozen"], {
            "site_id": site_id
        })
