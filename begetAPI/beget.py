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
    def __init__(self, login: str, password: str) -> None:
        self._backup = Backup(login, password)
        self._cron = Cron(login, password)
        self._dns = Dns(login, password)
        self._domain = Domain(login, password)
        self._ftp = Ftp(login, password)
        self._mail = Mail(login, password)
        self._mysql = Mysql(login, password)
        self._site = Site(login, password)
        self._stat = Stat(login, password)
        self._user = User(login, password)

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
