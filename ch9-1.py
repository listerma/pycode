# -*- coding: utf-8 -*-
# @Date    : 2018-01-14 21:40:51
# @Author  : brkstone
import socket
import os
import sys
import datetime


def resolve_uri(url):
    TYPE = "text/html\n\n"
    BODY = "<!DOCTYPE HTML><html><head><title>Directory</title></head>\n"
    BODY += "<h1>Hello World" + str(datetime.datetime.now()) + "</h1>"
    BODY += "<h2>url= " + url + "</h2>"
    BODY += "</body><html>"
    return TYPE, BODY


def parse_request(request):
    try:
        request = request.split("\r\n\r\n", 1)
        req = request[0].split("\r\n")
        for i, r in enumerate(req):
            req[i] = r.split()
        method = req[0][0].upper()
        url = req[0][1]
        print("url" + url)
        proto = req[0][2].upper()
        headers = {}
        for line in req[1:]:
            headers[line[0].upper()] = line[1:]
        if method == "GET":
            if proto == "HTTP/1.1" and "HOST:" in headers:
                return url
            else:
                raise SyntaxError("400 Bad Rrequest")
        else:
            raise ValueError("405 Method Not Allowed")
    except IndexError:
        raise SyntaxError("400 Bad Rrequest")


def response_ok(TYPE, BODY):
    return("HTTP/1.1 200 OK\r\n"
           "Content-Type:" + TYPE + "\r\n"
           "\r\n" + BODY)

# 例子缺少response_error函数，我随意增加的 ，socket还不清楚


def response_error(e):
    return "0"


def main():
    ADDR = ("127.0.0.1", 8888)
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen(1)
    while True:
        try:
            conn, addr = server.accept()
            s, msg = "", True
            while msg:
                msg = conn.recv(1024)
                s += msg
                if len(msg) < 1024:
                    break
            print(s)
            try:
                url = parse_request(s)
                TYPE, BODY = resolve_uri(url)
                resp = response_ok(TYPE, BODY)
            except (SyntaxError, ValueError, UserWarning) as e:
                resp = response_error(e)
        except KeyboardInterrupt as e:
            break
        except Exception as e:
            print("ERROR L:", e)
        print("resp", resp)

        conn.sendall(resp.encode())
        conn.close()


if __name__ == '__main__':
    main()
