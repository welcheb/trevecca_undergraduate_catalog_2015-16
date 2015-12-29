#!/usr/bin/env python

# import necessay modules
from lxml import html
from lxml import etree
import requests
import os
from requests_testadapter import Resp # pip install requests_testadapter

class LocalFileAdapter(requests.adapters.HTTPAdapter):
    def build_response_from_file(self, request):
        file_path = request.url[7:]
        with open(file_path, 'rb') as file:
            buff = bytearray(os.path.getsize(file_path))
            file.readinto(buff)
            resp = Resp(buff)
            r = self.build_response(request, resp)

            return r

    def send(self, request, stream=False, timeout=None,
             verify=True, cert=None, proxies=None):

        return self.build_response_from_file(request)

requests_session = requests.session()
requests_session.mount('file://', LocalFileAdapter())

# load majors page
majors_page = requests_session.get('file://./trevecca.html')
majors_tree = html.fromstring(majors_page.content.replace('&#13;',''))

# load minors page
minors_page = requests_session.get('file://./trevecca_minors.html')
minors_tree = html.fromstring(minors_page.content.replace('&#13;',''))

# print opening of combo web page
print '<!DOCTYPE html>'
print '<html class="no-js" lang="en-US" itemscope itemtype="http://schema.org/CollegeOrUniversity">' 

# print head open
print '<head>'
print '<title>http://trevecca.smartcatalogiq.com</title>'

# print majors css style links	
majors_style_links = majors_tree.xpath('//head/link')
for majors_style_link in majors_style_links:
    print(etree.tostring(majors_style_link, pretty_print=True))

# add page breaks before H1 and H2
print '<style type="text/css">'
print '@media print {'
print '    h1:not([name=first]){page-break-before: always;}'
print '    h2:not([name=first]){page-break-before: always;}'
print '}'
print '@media screen {'
print '    h1:not([name=first]){page-break-before: always;}'
print '    h2:not([name=first]){page-break-before: always;}'
print '}'
print '</style>'

# print head close
print '</head>'

# print body open
print '<body>'

# print majors body
elems = majors_tree.xpath('/html/body/div')
for elem in elems:
	print(etree.tostring(elem, pretty_print=True)).replace('<h2>','<h2 name="first">')

# print head close
print '<div id="main"><h1>Minors</h1></div>'

# print minors body
elems = minors_tree.xpath('/html/body/div')
for elem in elems:
	print(etree.tostring(elem, pretty_print=True)).replace('<h1 name="first">','<h1>',1)

# print closing of body and page
print '</body>'
print '</html>'
