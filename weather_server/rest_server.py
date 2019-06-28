#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Use tornado's `StaticFileHandler` to replace `SimpleHTTPServer` in Python
standard library, with this you can simply type only one command and run an
HTTP server on the port you desired, the default port [8000] is as the same
as the SimpleHTTPServer provided.
"""
import os
import sys
import logging
import signal

import tornado.web
import tornado.template
import tornado.websocket
import tornado.ioloop
import tornado.httpserver
from argparse import ArgumentParser
import json
#from tornado.options import options, define

from tornado.web import StaticFileHandler

__dir__ = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.INFO)

gtemp = 0.0
ghumi = 0.0

#------------------------------------------------------------------------------
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global gtemp
        global ghumi
        print("temp={} humi={}".format(gtemp, ghumi))
        items = ["Temperature: "+str(gtemp), "Humidity: "+str(ghumi)]
        self.render("template.html", title="Temperature monitor", items=items)

#------------------------------------------------------------------------------
class Info(tornado.web.RequestHandler):
    def get(self):
        global gtemp
        global ghumi
        global gwater
        logging.info('GET REST API')
        temp = self.get_arguments("temp")
        humi = self.get_arguments("humi")
        water = self.get_arguments("water")
        if temp == [] or humi == [] or water == []:
            self.set_status(400)
            return self.finish("Invalid recipe id")
        gtemp = float(temp[0])
        ghumi = float(humi[0])
        gwater = float(water[0])
        self.write("saved temp={} humi={} water={}".format(gtemp, ghumi, gwater))

#------------------------------------------------------------------------------
class Temperature_Handler(tornado.web.RequestHandler):
    def get(self):
        global gtemp
        logging.info('GET REST API')
        self.write("saved temp={}".format(gtemp))

#------------------------------------------------------------------------------
class Humidity_Handler(tornado.web.RequestHandler):
    def get(self):
        global gtemp
        logging.info('GET REST API')
        self.write("saved humidity={}".format(gtemp))

#------------------------------------------------------------------------------
class Water_Handler(tornado.web.RequestHandler):
    def get(self):
        global gtemp
        logging.info('GET REST API')
        self.write("saved water={}".format(gtemp))

#------------------------------------------------------------------------------
def parse_args(args=None):
    parser = ArgumentParser(
        description=(
            'Start a Tornado server '))
    parser.add_argument(
        '-p', '--port', type=int, default=8080,
        help='Port on which to run server.')
    return parser.parse_args(args)


#------------------------------------------------------------------------------
def stop_server(signum, frame):
    tornado.ioloop.IOLoop.instance().stop()
    logging.info('Stopped!')

#------------------------------------------------------------------------------
def run():
    args = parse_args()

    application = tornado.web.Application([
        (r"/setinfo", Info),
        (r'/', MainHandler),
        (r"/temperature", Temperature_Handler),
        (r"/humidity", Humidity_Handler),
        (r"/water", Water_Handler),
    ])
    signal.signal(signal.SIGINT, stop_server)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(args.port)
    logging.info('Weather Web server on port %d ...' % args.port)
    tornado.ioloop.IOLoop.instance().start()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    run()
