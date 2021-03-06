# -*- coding:utf-8 -**
__author__ = 'sunaihua'
from utils.ptime import fn_time

'''
列举出小于一个整数的所有素数
'''


def iter_list(num):
    # half_num = num / 2
    return range(2, num)


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    iter_nums = iter_list(num)
    if not iter_nums:
        return False
    for n in iter_nums:
        # print '%s/%s=%s' % (str(num), str(n), str(num % n))
        if num % n == 0:
            return False
    return True


def prime_list(max):
    for num in range(max):
        if is_prime(num):
            yield num


@fn_time
def main():
    # print len(list(prime_list(1000)))
    print list(prime_list(100000))


main()
