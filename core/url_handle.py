# -*- coding:utf-8 -*-
from importlib import import_module


def include(module):
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls


def url_wrapper(urls):
    '''
    拼接请求 url，调用对应的模块，如拼接 users 和 regist 成 url /users/regist，
    调用 views.users.users_views.RegistHandle 模块
    '''
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                # 分离获取字符串（如regist）和调用类（如views.users.users_views.RegistHandle）
                pattern, handle_class = handle
                # 拼接url，新的url调用模块
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list
