from .backup import Backup
from .cron import Cron
from .dns import Dns
from .domain import Domain
from .ftp import Ftp
from .mail import Mail
from .mysql import Mysql
from .site import Site
from .stat import Stat
from .user import User


class Beget:
    def __init__(self, *args, **kwargs) -> None:
        self._backup = Backup(*args, **kwargs)
        self._cron = Cron(*args, **kwargs)
        self._dns = Dns(*args, **kwargs)
        self._domain = Domain(*args, **kwargs)
        self._ftp = Ftp(*args, **kwargs)
        self._mail = Mail(*args, **kwargs)
        self._mysql = Mysql(*args, **kwargs)
        self._site = Site(*args, **kwargs)
        self._stat = Stat(*args, **kwargs)
        self._user = User(*args, **kwargs)

    @property
    def backup(self):
        return self._backup

    @property
    def cron(self):
        return self._cron

    @property
    def dns(self):
        return self._dns

    @property
    def domain(self):
        return self._domain

    @property
    def ftp(self):
        return self._ftp

    @property
    def mail(self):
        return self._mail

    @property
    def mysql(self):
        return self._mysql

    @property
    def site(self):
        return self._site

    @property
    def stat(self):
        return self._stat

    @property
    def user(self):
        return self._user
