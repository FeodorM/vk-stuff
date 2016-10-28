# vk-stuff
Scripts and functions, which is using vk api.

There is no tools/config.py and tools/people.py, you need to create them.

Write this into tools/config.py:

```python
app_id = 'app id'
login = 'your login'
password = 'your password'
```

there app_id is id of your app (you can create it [here](https://vk.com/apps?act=manage))

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
