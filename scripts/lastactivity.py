#!/usr/bin/env python3

import sys
import datetime

# path to tools/
# you need this, if you want to execute this script from anywhere, otherwise comment next line
sys.path.append('/home/satan/vk')

from tools import *


api = tools.create_api(MESSAGES)

# TODO: make cool args
for arg in sys.argv[1:]:
    if arg in dir(people):
        user_id = getattr(people, arg)
    else:
        try:
            user_id = int(arg)
        except ValueError:
            print('Incorrect username or id:', arg)
            continue

    res = datetime.datetime.fromtimestamp(api.messages.getLastActivity(user_id=user_id)['time'])

    print("{}:".format(arg))
    print(res)
    print(datetime.datetime.now(), '-- now\n')
