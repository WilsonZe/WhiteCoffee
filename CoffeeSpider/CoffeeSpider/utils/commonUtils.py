# -*- coding: utf-8 -*-
import hashlib
import re

import datetime


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def extract_num(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date

def extract_date(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+/\d+/\d+).*", text)
    if match_re:
        date = match_re.group(1)
    else:
        date = ""

    return date

if __name__ == "__main__":
    # print (get_md5("http://jobbole.com".encode("utf-8")))
    str = " 2017/6/11 评论"
    print(extract_date(str))