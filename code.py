# encode = utf-8
__author__ = 'haifwu@ebay.com'

import sys
import web
import urllib2

reload(sys)
sys.setdefaultencoding('UTF-8')

urls = (
    '/google', 'google',
    '/(.*)', 'index'
)

class google:
    def GET(self):
        data = urllib2.urlopen("http://www.baidu.com/s?wd=beauti&rsv_spt=1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=7&rsv_pq=da90cf1600019ea5&rsv_t=c115qqtafaTVz4xy3js5pRv%2BQy5ZBKSDz0%2BSMvBhbQE4dE39ClQFU8q2TqtKKC8j41sV&rsv_sug2=0&inputT=2375&rsv_sug4=4225").read()
        print data
        return data

class index:
    def GET(self, name):
        return 'Hello world!' + name

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

