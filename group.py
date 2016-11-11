from datetime import datetime
from pprint import pprint
from time import sleep

from tools import *

text = 'Сегодня ничего не произошло.'

api = tools.create_api()
r = api.execute(
    code=open('js/group.js').read()
)
for post in r:
    if post['text'] != text:
        date = datetime.fromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M:%S')
        print(date, post['text'])
