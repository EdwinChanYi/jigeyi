import sys
import traceback
import Ice
import json
from flup.server.fcgi import WSGIServer
def HttpReqHandler(environ, start_response):
  try:
    status = '200 OK'
    response_headers = [('Content-Type', 'text/json')]
    start_response(status, response_headers)
    return ["hello world"]
  except:
    pass

if __name__ =='__main__':
  WSGIServer(HttpReqHandler, bindAddress=('127.0.0.1',8088)).run()
