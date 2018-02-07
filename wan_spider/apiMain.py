# coding=utf-8

import urllib2
from head_filter import *

def get():
    print REQUEST_HEAD
    print get_request_body_rows()
    req = urllib2.Request(REQUEST_URL,get_request_body_rows(),REQUEST_HEAD)
    res = urllib2.urlopen(req).read()
    print res

get()