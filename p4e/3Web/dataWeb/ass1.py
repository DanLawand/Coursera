import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_800034.xml'

try:
    varxml = urllib.request.urlopen(url, context=ctx).read()
except:
    print('Wrong URL')
    quit()

treeCommentinfo = ET.fromstring(varxml)
# ('comments/comment/count') == ('.//count')
counts = treeCommentinfo.findall('.//count')
soma = 0
for count in counts:
    soma = soma + int((count.text))
print('Sum:', soma)
