#! python

import sys
import urllib.request

if len(sys.argv) == 1:
    proxy_url = sys.argv[1]
    print ("requesting: %s " % str(proxy_url))
    urllib.request.urlopen(proxy_url)
