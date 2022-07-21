from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Domain(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["domain"]

    async def get_list(self) -> Answer:
        return await self._do_request(self._rest["get_list"])

    async def get_zone_list(self) -> Answer:
        return await self._do_request(self._rest["get_zone_list"])

    async def add_virtual(self, hostname: str, zone_id: int) -> Answer:
        return await self._do_request(self._rest["add_virtual"], {
            "hostname": hostname,
            "zone_id": zone_id
        })

    async def delete(self, id: int) -> Answer:
        return await self._do_request(self._rest["delete"], {
            "id": id
        })

    async def get_subdomain_list(self) -> Answer:
        return await self._do_request(self._rest["get_subdomain_list"])

    async def add_subdomain_virtual(self, subdomain: str, domain_id: int) -> Answer:
        return await self._do_request(self._rest["add_subdomain_virtual"], {
            "subdomain": subdomain,
            "domain_id": domain_id
        })

    async def delete_subdomain(self, id: int) -> Answer:
        return await self._do_request(self._rest["delete_subdomain"], {
            "id": id
        })

    async def check_domain_to_register(self, hostname: str, zone_id: int, period: int) -> Answer:
        return await self._do_request(self._rest["check_domain_to_register"], {
            "hostname": hostname,
            "zone_id": zone_id,
            "period": period
        })

    async def get_php_version(self, full_fqdn: str) -> Answer:
        return await self._do_request(self._rest["get_php_version"], {
            "full_fqdn": full_fqdn
        })

    async def change_php_version(self, full_fqdn: str, php_version: str, is_cgi: bool=False) -> Answer:
        return await self._do_request(self._rest["change_php_version"], {
            "full_fqdn": full_fqdn,
            "php_version": php_version,
            "is_cgi": is_cgi
        })

    async def get_directives(self, full_fqdn: str) -> Answer:
        return await self._do_request(self._rest["get_directives"], {
            "full_fqdn": full_fqdn
        })

    async def add_directives(self, full_fqdn: str, directives_list: list) -> Answer:
        return await self._do_request(self._rest["add_directives"], {
            "full_fqdn": full_fqdn,
            "directives_list": directives_list
        })

    async def remove_directives(self, full_fqdn: str, directives_list: list) -> Answer:
        return await self._do_request(self._rest["remove_directives"], {
            "full_fqdn": full_fqdn,
            "directives_list": directives_list
        })
