import vk
import phonenumbers

from typing import List, Union, Callable, Dict, Any
from time import sleep

from tools.config import *


def format_phone(phone: phonenumbers.PhoneNumber) -> str:
    return phonenumbers.format_number(
        phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)


def create_api(configs: Union[List[str], str] = '') -> vk.API:
    return vk.API(vk.AuthSession(
        app_id, login, password,
        v='5.59',
        scope=','.join(configs) if not isinstance(configs, str) else configs)
    )


# TODO: use execute
def for_each_through_history(api, func: Callable[[Dict[str, Any]], None], user_id: Union[int, str]) -> None:
    """
    Applies function func to each message in chat with user_id
    """
    amount = api.messages.getHistory(user_id=user_id, count=1)[0]

    for offset in range(0, amount + 200, 200):
        res = api.messages.getHistory(
            user_id=user_id,
            rev=1,
            count=200,
            offset=offset
        )

        [func(message) for message in res['items']]

        print('{} messages checked'.format(offset))
        sleep(.3)
