from typing import Coroutine, Union

from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Mail(Request):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._rest = REST_API["mail"]

    def get_mailbox_list(self, domain: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["get_mailbox_list"], {
            "domain": domain
        })

    def change_mailbox_password(self, domain: str, mailbox: str, mailbox_password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["change_mailbox_password"], {
            "domain": domain,
            "mailbox": mailbox,
            "mailbox_password": mailbox_password
        })

    def create_mailbox(self, domain: str, mailbox: str, mailbox_password: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["create_mailbox"], {
            "domain": domain,
            "mailbox": mailbox,
            "mailbox_password": mailbox_password
        })

    def drop_mailbox(self, domain: str, mailbox: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["drop_mailbox"], {
            "domain": domain,
            "mailbox": mailbox
        })

    def change_mailbox_settings(self, domain: str, mailbox: str, spam_filter_status: bool,
                                spam_filter: int, forward_mail_status: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["change_mailbox_settings"], {
            "domain": domain,
            "mailbox": mailbox,
            "spam_filter_status": spam_filter_status,
            "spam_filter": spam_filter,
            "forward_mail_status": forward_mail_status
        })

    def forward_list_add_mailbox(self, domain: str, mailbox: str, forward_mailbox: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["forward_list_add_mailbox"], {
            "domain": domain,
            "mailbox": mailbox,
            "forward_mailbox": forward_mailbox
        })

    def forward_list_delete_mailbox(self, domain: str, mailbox: str, forward_mailbox: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["forward_list_delete_mailbox"], {
            "domain": domain,
            "mailbox": mailbox,
            "forward_mailbox": forward_mailbox
        })

    def forward_list_show(self, domain: str, mailbox: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["forward_list_show"], {
            "domain": domain,
            "mailbox": mailbox,
        })

    def set_domain_mail(self, domain: str, domain_mailbox: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["set_domain_mail"], {
            "domain": domain,
            "domain_mailbox": domain_mailbox
        })

    def clear_domain_mail(self, domain: str) -> Union[Answer, Coroutine]:
        return self._do_request(self._rest["clear_domain_mail"], {
            "domain": domain
        })
