一.框架搭建
1）安装软件
python下载地址：
http://www.python.org/
webpy下载地址：
http://webpy.org/
flup下载地址：
http://trac.saddi.com/flup
nginx下载地址：
http://nginx.org/en/download.html
spawn-fcgi下载地址：
http://redmine.lighttpd.net/projects/spawn-fcgi/news
2）nginx配置
[python] view plain copy
server{  
     listen       80;  
     server_name  www.test.com;  
     root /path/to/web/root;  
     access_log  logs/www.xx.com.access.log  main;  
   
     location / {  
         include fastcgi_params;   ##包含默认的fastcgi参数  
         fastcgi_param SCRIPT_FILENAME $fastcgi_script_name;    
         fastcgi_param PATH_INFO $fastcgi_script_name;         
         fastcgi_pass 127.0.0.1:9002;                  ##把请求通过fastcgi传送给本机的9002端口  
     }  
   
     location /static/ {                    #配置静态文件的访问  
         if (-f $request_filename) {        #如果请求文件名是一个文件  
         rewrite ^/static/(.*)$  /static/$1 break;   #直接跳转到对应的资源，中断fastcgi的传输  
         }  
     }  
}
3）webpy
[python] view plain copy
#!/usr/bin/env python  
# -*- coding: utf-8 -*-     

import web     
urls = ("/.*", "hello")  
app = web.application(urls, globals())   
class hello:  
	def GET(self):  
		return 'Hello, world!'     
   
if __name__ == "__main__":  
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)   ##这行是新增的  
	 app.run()  
4）启动code.py
spawn-fcgi -d /path/to/www -f /path/to/www/code.py -a 127.0.0.1 -p 9002   #端口和nginx配置里要一致
-f 指定调用FastCGI的web文件，web程序的入口文件，即code.py文件
-d 指定web程序的主目录，即code.py所在的目录
-a 绑定到地址 addr
-p 绑定到端口 port
-F 指定产生的 FastCGI 的进程数
-P 指定产生的进程的 PID 文件路径
-u 和 -g FastCGI 使用什么身份运行
可以将进程PID保存下来方便关闭进程：
kill `cat /tmp/zcut.pid`

