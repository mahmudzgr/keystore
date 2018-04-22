#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os
from passGenerator import *
from PasswordGenerator import PasswordGenerator



class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        rootdir = os.path.dirname(os.path.abspath(__file__)) + '/public'  # file location
        try:
            if (self.path.startswith('/api') is False) and self.path.endswith('.html'):
                print(rootdir + self.path)
                f = open(rootdir + self.path, 'r')  # open requested file

                # send code 200 response
                self.send_response(200)

                # send header first
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # send file content to client
                self.wfile.write(f.read().encode())
                f.close()
            elif urlparse(self.path).path == '/api/password':
                query = parse_qs(urlparse(self.path).query)
                length = int(query['length'][0])
                digits = query['digits'][0]
                specials = query['specials'][0]


                if length < 4:
                    self.send_response(500)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("Password has to composed of at least 4 characters!".encode())
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    self.wfile.write('Length :\t{}<br>Digits :\t{}<br>Specials :\t{}<br><br>Password :\t'.format(length,digits,specials).encode())

                    self.wfile.write("{}".format(passGenerator(length,digits,specials)).encode())
            elif urlparse(self.path).path == '/api/password2':
                query = parse_qs(urlparse(self.path).query)
                length = 16
                if 'length' in query:
                    length = int(query['length'][0])
                lowercase = False
                if 'lowercase' in query:
                    lowercase = query['lowercase'][0] == 'on'
                uppercase = False
                if 'uppercase' in query:
                    uppercase = query['uppercase'][0] == 'on'
                digits = False
                if 'digits' in query:
                    digits = query['digits'][0] == 'on'
                specials = False
                if 'specials' in query:
                    specials = query['specials'][0] == 'on'

                if length < 4:
                    self.send_response(500)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("Password has to composed of at least 4 characters!".encode())
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    self.wfile.write('Length :\t{}<br>Digits :\t{}<br>Specials :\t{}<br><br>Password :\t'.format(length,digits,specials).encode())

                    passgen = PasswordGenerator()
                    passgen.set(lowercase, uppercase, digits, specials)

                    self.wfile.write(passgen.generate(length).encode())

            return

        except IOError:
            self.send_error(404, 'file not found')
        return

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        print("Server works on http://localhost:8000")
        print("Server works on http://localhost:8000/api/password?length=16&digits=on&specials=on")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stop the server on http://localhost:8000")
        httpd.socket.close()


if __name__ == '__main__':
    run()
