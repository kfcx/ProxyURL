# -*- coding: utf-8 -*-
# @Time    : 2022/10/8
# @Author  : Naihe
# @File    : __init__.py
# @Software: PyCharm
from loguru import *
import sys
from fastapi import *
from apscheduler.executors.pool import *
import logging
import base64
from apscheduler.schedulers.background import *
from apscheduler.triggers.cron import *
from app.conf import *
from app.plugins.proxy.tasks import *
from .v2 import *
from ..conf.config import *
from ..scheams.response import *


def init_app():
    app = FastAPI(
        title=config.TITLE,
        description=config.DESC,
        version=config.VERSION,
        debug=DEBUG
    )
    return app


app = init_app()
app.include_router(v2)


@app.get('/')
async def Root_Path():
    data = {
        "API_status": "Running",
        "Version": config.VERSION,
        "Web_APP": "https://proxy.naihe.me/",
        "API_Document": "https://proxy.naihe.me/docs",
        "GitHub": "https://github.com/kfcx/proxyURL",
    }
    return JSONResponse(data)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
