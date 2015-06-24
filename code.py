# encode = utf-8
__author__ = 'haifwu@ebay.com'

import sys
import web
import urllib2
import urllib
import json

reload(sys)
sys.setdefaultencoding('UTF-8')

urls = (
    '/google', 'google',
    '/search', 'search',
    '/(.*)', 'index'
)


class google:
    def GET(self):
        data = open("./Google.html", "r").read()
        return data

class search:
    def GET(self):
	    query = urllib.urlencode({'q': web.input().q})
	    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	    print url
	    head = "<!DOCTYPE html><html><head><title>Search Result</title></head><body>"
	    data = urllib2.urlopen(url).read()
	    results = json.loads(data)
	    data = results['responseData']
	    ret = 'Total results: ' + data['cursor']['estimatedResultCount'] + "<br>"
	    hits = data['results']
	    ret += 'Top %d hits:' % len(hits) + "<br>"
	    for h in hits: ret += "&nbsp"*4 +' <a href="' + h['url'] + '">' +  h['url'] + '</a>' + "<br>"
	    ret += 'For more results, see <a href="%s"> %s </a>' % (data['cursor']['moreResultsUrl'], data['cursor']['moreResultsUrl'])
	    return head + ret + "</body></html>"

class index:
    def GET(self, name):
        url = "https://www.google.com/" + name
	print "-"*10 + url 
	data = urllib2.urlopen(url).read()
	return data 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

