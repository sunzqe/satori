# -*- coding: utf-8 -*-
from __future__ import absolute_import

# -- stdlib --
# -- third party --
import requests

# -- own --
from backend.common import register_backend
from utils import status2emoji


# -- code --
@register_backend
def yunpian_sms(conf, user, event):
    if not user.get('phone'):
        return

    msg = u'【%s】%s[P%s]\n%s\n' % (
        conf['signature'],
        status2emoji(event['status']),
        event['level'],
        event['title'],
    ) + event['text']

    rst = requests.post('http://yunpian.com/v1/sms/send.json', data={
        'apikey': conf['api_key'],
        'mobile': user['phone'],
        'text': msg,
    }).json()

    if rst['code'] != 0:
        raise Exception(rst['detail'])
