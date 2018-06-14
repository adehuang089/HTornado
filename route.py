# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from core.url_handle import include

urls = [
    (r"/", include('app.router.index'))
]
