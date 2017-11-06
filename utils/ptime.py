# -*- coding:utf-8 -**
import time
from functools import wraps

'算法执行时间计数器'
__author__ = 'sunaihua'


def fn_time(function):
    @wraps(function)
    def func_timer(*args, **kwargs):
        s_time = time.time()
        result = function(*args, **kwargs)
        print ("Total time running %s: %s seconds" % (function.func_name, str(time.time() - s_time)))
        return result

    return func_timer
