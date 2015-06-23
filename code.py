# encode = utf-8
__author__ = 'haifwu@ebay.com'

import sys
import web

reload(sys)
sys.setdefaultencoding('UTF-8')

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return 'Hello world!'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

