#!/usr/bin/env python
# coding:utf-8
# Chinese identity card post 6/8 numbers build plugins base on diff sex
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
from lib.fun import finishprinter, finishcounter, range_compatible
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, IDCARD_prefix, filextension, plug_range, sex_range


def get_idcard_post(posflag, encodeflag, head, tail, sex):
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s_%s%s" %
                             (IDCARD_prefix, str(posflag)[-1:], get_buildtime(), encodeflag, filextension))
    posrule = lambda _: str(_) if _ >= 10 else "0" + str(_)
    # month
    value1112 = " ".join(posrule(x) for x in range_compatible(1, 13))
    # day
    value1314 = " ".join(posrule(x) for x in range_compatible(1, 32))
    value1516 = " ".join(posrule(x) for x in range_compatible(1, 100))
    post18 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X")
    value1718 = ""
    if sex == sex_range[0]:
        rand = ("1", "3", "5", "7", "9")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif sex == sex_range[1]:
        rand = ("0", "2", "4", "6", "8")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif sex == sex_range[2]:
        rand = " ".join(str(_) for _ in range_compatible(0, 10))
        for _ in rand.split(" "):
            for _p in post18:
                value1718 += _ + _p + " "

    with open(storepath, "a") as f:
        if posflag == plug_range[1]:
            for v1112 in value1112.split(" "):
                for v1314 in value1314.split(" "):
                    for v1516 in value1516.split(" "):
                        for v1718 in value1718.split(" "):
                            if v1718 != "":
                                f.write(operator.get(encodeflag)(head + v1112 + v1314 + v1516 + v1718 + tail) + CRLF)
        elif posflag == plug_range[0]:
                for v1314 in value1314.split(" "):
                    for v1516 in value1516.split(" "):
                        for v1718 in value1718.split(" "):
                            if v1718 != "":
                                f.write(operator.get(encodeflag)(head + v1314 + v1516 + v1718 + tail) + CRLF)
    finishprinter(finishcounter(storepath), storepath)
