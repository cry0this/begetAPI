import json


class Answer:
    def __init__(self, raw_text: str) -> None:
        self._is_parsed = False
        self._is_success = False
        self._error_text = ""
        self._error_code = ""
        self._json = {}

        self._raw = raw_text
        
        try:
            json_data = json.loads(self._raw)
        except json.decoder.JSONDecodeError:
            return

        self._is_parsed = True

        if json_data["status"] == "error":
            self._error_text = json_data["error_text"]
            self._error_code = json_data["error_code"]
        
        if json_data["status"] == "success":
            self._is_success = True
            self._json = json_data["answer"]

    @property
    def raw(self) -> str:
        return self._raw

    @property
    def is_parsed(self) -> bool:
        return self._is_parsed

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def error_text(self) -> str:
        return self._error_text

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def json(self) -> dict:
        return self._json
