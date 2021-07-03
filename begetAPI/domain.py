from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Domain(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["domain"]

    def get_list(self) -> Answer:
        return self._do_request(self._rest["get_list"])

    def get_zone_list(self) -> Answer:
        return self._do_request(self._rest["get_zone_list"])

    def add_virtual(self, hostname: str, zone_id: int) -> Answer:
        return self._do_request(self._rest["add_virtual"], {
            "hostname": hostname,
            "zone_id": zone_id
        })

    def delete(self, id: int) -> Answer:
        return self._do_request(self._rest["delete"], {
            "id": id
        })

    def get_subdomain_list(self) -> Answer:
        return self._do_request(self._rest["get_subdomain_list"])

    def add_subdomain_virtual(self, subdomain: str, domain_id: int) -> Answer:
        return self._do_request(self._rest["add_subdomain_virtual"], {
            "subdomain": subdomain,
            "domain_id": domain_id
        })

    def delete_subdomain(self, id: int) -> Answer:
        return self._do_request(self._rest["delete_subdomain"], {
            "id": id
        })

    def check_domain_to_register(self, hostname: str, zone_id: int, period: int) -> Answer:
        return self._do_request(self._rest["check_domain_to_register"], {
            "hostname": hostname,
            "zone_id": zone_id,
            "period": period
        })

    def get_php_version(self, full_fqdn: str) -> Answer:
        return self._do_request(self._rest["get_php_version"], {
            "full_fqdn": full_fqdn
        })

    def change_php_version(self, full_fqdn: str, php_version: str, is_cgi: bool=False) -> Answer:
        return self._do_request(self._rest["change_php_version"], {
            "full_fqdn": full_fqdn,
            "php_version": php_version,
            "is_cgi": is_cgi
        })

    def get_directives(self, full_fqdn: str) -> Answer:
        return self._do_request(self._rest["get_directives"], {
            "full_fqdn": full_fqdn
        })

    def add_directives(self, full_fqdn: str, directives_list: list) -> Answer:
        return self._do_request(self._rest["add_directives"], {
            "full_fqdn": full_fqdn,
            "directives_list": directives_list
        })

    def remove_directives(self, full_fqdn: str, directives_list: list) -> Answer:
        return self._do_request(self._rest["remove_directives"], {
            "full_fqdn": full_fqdn,
            "directives_list": directives_list
        })
