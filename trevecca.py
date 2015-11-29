#!/usr/bin/env python

# import necessay modules
from lxml import html
from lxml import etree
import requests

# top-level domain
parent_domain = 'http://trevecca.smartcatalogiq.com'

# parent page showing the porgrams of study
parent_page_url = parent_domain + '/en/2015-2016/University-Catalog/Programs-of-Study'
parent_page = requests.get(parent_page_url)
parent_tree = html.fromstring(parent_page.content)

# get list of program names and program URLs
program_names = parent_tree.xpath('//div[@id="sc-program-links"]//a//text()')
program_links = parent_tree.xpath('//div[@id="sc-program-links"]//a//@href')

# print opening of web page
print '<!DOCTYPE html>'
print '<html class="no-js" lang="en-US" itemscope itemtype="http://schema.org/CollegeOrUniversity">' 

# loop over programs
for program_idx in range(len(program_names)):
	program_page_url = parent_domain + program_links[program_idx]
	program_page = requests.get(program_page_url)
	program_tree = html.fromstring(program_page.content)
	program_div = program_tree.xpath('//div[@id="main"]')

	if program_idx==0:
		print '<head>'
		print '<title>' + parent_domain + '</title>'	

		# css style links	
		program_style_links = program_tree.xpath('//head/link')
		for program_style_link in program_style_links:	
			print(etree.tostring(program_style_link, pretty_print=True).replace('href="', 'href="' + parent_domain))

		# add page breaks before H1 (program names)
		print '<style type="text/css">'
		print '@media print {'
		print '    h1:not([name=first]){page-break-before: always;}'
		print '}'
		print '@media screen {'
		print '    h1:not([name=first]){page-break-before: always;}'
		print '}'
		print '</style>'

		print '</head>'
		print '<body>'

		print(etree.tostring(program_div[0],pretty_print=True).replace('href="', 'href="' + parent_domain).replace('<h1>', '<h1 name="first">', 1))

	else:
		print(etree.tostring(program_div[0],pretty_print=True).replace('href="', 'href="' + parent_domain))

	# uncomment for quicker debug
	#if program_idx>2:
	#	break

# print closing of body and page
print '</body>'
print '</html>'



