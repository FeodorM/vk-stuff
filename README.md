# vk-stuff
Scripts and functions, which is using vk api.

There is no tools/config.py and tools/people.py, you need to create them.

Write this into tools/config.py:

```python
APP_ID = 'app id'
LOGIN = 'your login'
PASSWORD = 'your password'
DIR = '/path/to/cloned/dir/vk-stuff'
PHONE_NUMBER = '88005553535'
```

there APP_ID is id of your app (you can create it [here](https://vk.com/apps?act=manage)) and
PHONE_NUMBER is default number to send sms with smssend.py  

tools/people.py is a file where you can store ids, e.g.

```python
durov = 1
my_group = 123456789
```

Example of usage:
```python
from tools import *

api = tools.create_api(MESSAGES)

# print last message in the chat with user with id 1
print(api.messages.getHistory(user_id=1)['items'][0])

# same, but if you have username in people.py
print(api.messages.getHistory(user_id=people.username)['items'][0])
```
