# -*- coding: utf-8 -*-
# @Time    : 2023/1/12
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : cache_tools.py
# @Software: PyCharm
import time
from base64 import b64encode
import aiohttp
import itertools
import requests
from loguru import *
from threading import *
from collections import *
from urllib.parse import *
from app.conf.config import *
from app.plugins.proxy.tools import *
from curl_cffi import requests


async def processing(url, data):
    for _temp in data:
        if ".ts" in _temp:
            if not is_url(_temp):
                yield "/file.ts?x=" + b64encode(_temp.encode("utf-8")).decode("utf-8")
            else:
                yield "/file.ts/?x=" + b64encode(urljoin(url, _temp).encode("utf-8")).decode("utf-8")
        else:
            yield _temp
        yield "\n"


def download(url):
    if _temp_ts := ts_info.get(url):
        return _temp_ts
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    }
    with requests.get(url=url, headers=header, impersonate="chrome") as res:
        _data = res.content
        ts_info[url] = _data
        return _data


def get_m3u8_down(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    with requests.get(url=url, headers=headers, impersonate="chrome") as res:
        _data = res.text
        return _data
