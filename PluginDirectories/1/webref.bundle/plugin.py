#!/usr/bin/python

import sys,urllib,os

def results(fields, original_query):
    if '~html' in fields:
        sub = 'html'
        tag = fields['~html']
    elif '~css' in fields:
        sub = 'css'
        tag = fields['~css']
    else:
        return
        {
            "title": "Print something"
        }
    html = open("webref.html").read().replace("<!--SUB-->", sub).replace("<!--TAG-->",tag)
    return {
        "title": "Search {0} manual for '{1}'".format(sub,tag),
        "html":html,
        "webview_transparent_background": False,
        "run_args":[sub,tag]
    }

def run(sub,tag):
    os.system('open "http://webref.ru/{0}/{1}"'.format(urllib.quote(sub),urllib.quote(tag)))
