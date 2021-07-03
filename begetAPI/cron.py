from .__rest_api import REST_API
from .__request import Request
from .__answer import Answer


class Cron(Request):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)
        self._rest = REST_API["cron"]

    def get_list(self) -> Answer:
        return self._do_request(self._rest["get_list"])

    def add(self, minutes: str, hours: str, days: str, months: str, 
            weekdays: str, command: str) -> Answer:
        return self._do_request(self._rest["add"], {
            "minutes": minutes,
            "hours": hours,
            "days": days,
            "months": months,
            "weekdays": weekdays,
            "command": command
        })

    def edit(self, id: int, minutes: str, hours: str, days: str, 
             months: str, weekdays: str, command: str) -> Answer:
        return self._do_request(self._rest["edit"], {
            "id": id,
            "minutes": minutes,
            "hours": hours,
            "days": days,
            "months": months,
            "weekdays": weekdays,
            "command": command
        })

    def delete(self, row_number: int) -> Answer:
        return self._do_request(self._rest["delete"], {
            "row_number": row_number
        })

    def change_hidden_state(self, row_number: int, is_hidden: bool) -> Answer:
        return self._do_request(self._rest["change_hidden_state"], {
            "row_number": row_number,
            "is_hidden": is_hidden
        })

    def get_email(self) -> Answer:
        return self._do_request(self._rest["get_email"])

    def set_email(self, email: str) -> Answer:
        return self._do_request(self._rest["set_email"], {
            "email": email
        })
