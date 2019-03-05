# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='password', db='awesome')
    u = User(name='Test', email='test@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    # 下面一行配合orm.py中的destory_pool()函数使用
    await orm.destory_pool()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    # 也可以是test()函数中的最后一行代码:
    # if loop.is_closed():
    #     exit(0)
