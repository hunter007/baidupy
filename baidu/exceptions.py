# -*- coding:utf-8 -*-
from __future__ import unicode_literals


class BaiduException(Exception):
    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def __unicode__(self):
        return '<BaiduException {0}>'.format(self.errcode)
