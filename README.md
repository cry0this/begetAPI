# begetAPI

---

Unofficial wrapper for [Beget.API](https://beget.com/ru/kb/api/beget-api)
Requires python >= 3.6

## Installation
```
pip install begetAPI
```


## How to use
Just include Beget class
```
from begetAPI import Beget

beget = Beget("login", "password")
answer = beget.user.get_account_info()
```

or you can include specific class
```
from begetAPI import User

user = User("login", "password")
answer = user.get_account_info()
```

See [Beget.API](https://beget.com/ru/kb/api/beget-api) documentation to get list of methods.

For asynchronous calls you can add `asynchronous` param (False by default):
```
beget = Beget("login", "password", asynchronous=True)
```

## Answer class
All methods returns Answer() class with properties:
- **raw**(str): contains raw response string
- **is_parsed**(bool): `False` if failed to parse json from raw string
- **is_success**(bool): `True` if `status` field equals "success"
- **error_text**(str): contains `error_text` field
- **error_code**(str): contains `error_code` field
- **json**(dict): contains parsed data from `answer` field

For example:
```
>>> answer = beget.cron.get_list()
>>> answer.raw
'{"status":"success","answer":{"status":"success","result":[{"row_number":1964545,"minutes":"*\\/10","hours":"*","days":"*","months":"*","weekdays":"*","command":"\\/usr\\/local\\/bin\\/php7.2 ~\\/test.php","is_hidden":0}]}}'
>>> answer.is_parsed
True
>>> answer.is_success
True
>>> answer.json["result"][0]["row_number"]
1964545
```

When received error:
```
>>> answer = beget.site.get_list()
>>> answer.raw
'{"status":"error","error_text":"Username\\/password incorrect","error_code":"AUTH_ERROR"}'
>>> answer.is_success
False
>>> answer.error_text
'Username/password incorrect'
>>> answer.error_code
'AUTH_ERROR'
```
