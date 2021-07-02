import json

class Answer:
    def __init__(self, raw_text: str) -> None:
        self._raw = raw_text
        self._success = False
        self._error_text = ""
        self._error_code = ""
        self._answer = {}
        
        try:
            json_data = json.loads(self._raw)
        except json.decoder.JSONDecodeError:
            return

        if "status" not in json_data.keys():
            self._answer = json_data
            return
        
        if json_data["status"] == "error":
            self._error_text = json_data["error_text"]
            self._error_code = json_data["error_code"]
        
        if json_data["status"] == "success":
            self._success = True
            self._answer = json_data["answer"]

    @property
    def raw(self):
        return self._raw

    @property
    def success(self):
        return self._success

    @property
    def error_text(self):
        return self._error_text

    @property
    def error_code(self):
        return self._error_code

    @property
    def answer(self):
        return self._answer
