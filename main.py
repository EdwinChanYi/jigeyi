import sys
import traceback
import Ice
import json
from flup.server.fcgi import WSGIServer
def HttpReqHandler(environ, start_response):
	ret=""
	try:
		uri=environ['PATH_INFO']
		print uri
		if uri[-1]=="/":
			uri=uri[:-1]
			if uri=="":
				ret=str(environ)
			elif uri=="/sleep":
				time.sleep(5)
				ret="sleep 5 seconds"
			else:
				ret=uri
	except Exception,e:
		ret=str(e)			
	status = '200 OK'
	response_headers = [('Content-Type', 'text/json')]
	start_response(status, response_headers)
	return [ret]

if __name__ =='__main__':
  WSGIServer(HttpReqHandler, bindAddress=('127.0.0.1',8088)).run()
