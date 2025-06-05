import os
import uuid
import hashlib
import requests
from pathlib import *
from loguru import *
from typing import *
from configparser import *
from pydantic import *
from platform import *


class Config(BaseSettings):
    TITLE: Optional[str] = "ProxyURL"

    DESC: Optional[str] = """
#### Description/说明
<details>
<summary>点击展开/Click to expand</summary>
- 频道源代理后播放更稳定，更多功能正在开发中。
- 如果需要更多接口，请查看[https://proxy.naihe.me/docs](https://proxy.naihe.me/docs)。
- 本项目开源在[GitHub：ProxyURL](https://github.com/239144498/ProxyURL)。
- 本项目不提供IPTV频道源，请自行搜索。
- 如遇到问题或BUG或建议请在[issues](https://github.com/239144498/ProxyURL/issues)中反馈。
- 本项目仅供学习交流使用，严禁用于违法用途，如有侵权请联系作者。
</details>
#### Contact author/联系作者
<details>
<summary>点击展开/Click to expand</summary>
- WeChat: onaihe
- Email: [239144498@qq.com](mailto:239144498@qq.com)
- Github: [https://github.com/239144498](https://github.com/239144498)
</details>
    """

    VERSION = "1.0"

    ORIGINS = [
        "*"
    ]

    ROOT = Path()

    LOG_DIR = ROOT / "log"

    datadir = ROOT / 'vtemp'

    count = 0

    url_regex = r"(http|https)://((?:[\w-]+\.)+[a-z0-9]+)((?:\/[^/?#]*)+)?(\?[^#]+)?(#.+)?"


logger.info("配置加载中...")
config = Config()

request = requests.session()

try:
    cfg = ConfigParser()
    cfg.read(config.ROOT / "assets/config.ini", encoding="utf-8")
    redis_cfg = dict(cfg.items("redis"))
    mysql_cfg = dict(cfg.items("mysql"))
    default_cfg = dict(cfg.items("default"))
    advanced_cfg = dict(cfg.items("advanced"))
    PORT = int(os.getenv("PORT", default=default_cfg.get("port")))

    authkey = default_cfg.get("authkey")
    vbuffer = int(default_cfg.get("vbuffer"))
    localhost = os.environ.get("localhost") or default_cfg.get("localhost")
    defaultdb = default_cfg.get("defaultdb")
    active_mode = eval(default_cfg.get("active_mode", "False"))

    host1 = advanced_cfg.get("host1")
    host2 = advanced_cfg.get("host2")
    tvglogo = advanced_cfg.get("tvglogo")
    DEBUG = eval(os.getenv("DEBUG", default=advanced_cfg.get("debug", "False")))
except:
    DEBUG = True
    PORT = 8080
mac = uuid.UUID(int=uuid.getnode()).hex
mdata = hashlib.md5(config.VERSION.encode())

headers = {
    'Content-Type': 'video/MP2T',
    'Cache-Control': 'max-age=600',
    'Accept-Ranges': 'bytes'
}
headers2 = {
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Content-Type': 'application/vnd.apple.mpegurl',
    'Expires': '-1',
}
try:
    tx = 1
except Exception as e:
    tx = 0

ts_info = {}

gdata = None
logger.info("配置加载完成")

