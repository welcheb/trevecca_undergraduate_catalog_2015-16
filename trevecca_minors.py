#!/usr/bin/env python

# import necessay modules
from lxml import html
from lxml import etree
import requests

# top-level domain
parent_domain = 'http://trevecca.smartcatalogiq.com'

# parent page showing the porgrams by schools and departments
parent_page_url = parent_domain + '/en/2015-2016/University-Catalog/Programs-by-Schools-and-Departments'
parent_page = requests.get(parent_page_url)
parent_tree = html.fromstring(parent_page.content)

# get list of potential department names and potential department URLs
department_names = parent_tree.xpath('//div[@id="main"]//p[@class="sc-BodyTextIndented"]//a//text()')
department_links = parent_tree.xpath('//div[@id="main"]//p[@class="sc-BodyTextIndented"]//a//@href')

# print opening of web page
print '<!DOCTYPE html>'
print '<html class="no-js" lang="en-US" itemscope itemtype="http://schema.org/CollegeOrUniversity">' 

# flag to detect first department
first_department_found = 0

# loop over departments
for department_idx in range(len(department_names)):

	# only use names containing "Department"
	if department_names[department_idx].find("Department")>=0: 

		# flag to detect first minor per department
		first_minor_found = 0

		department_page_url = parent_domain + department_links[department_idx]
		department_page = requests.get(department_page_url)
		department_tree = html.fromstring(department_page.content)

		# find potential links to minors
		minor_names = department_tree.xpath('//div[@id="main"]//a//text()')
		minor_links = department_tree.xpath('//div[@id="main"]//a//@href')

		for minor_idx in range(len(minor_names)):

			# only use names containing "Minor"
		        if minor_names[minor_idx].find("Minor")>0:

				minor_page_url = parent_domain + minor_links[minor_idx]
        		        minor_page = requests.get(minor_page_url)
                		minor_tree = html.fromstring(minor_page.content)

				# find potential links to minors (layer 2)
                		minor2_names = minor_tree.xpath('//div[@id="main"]//a//text()')
                		minor2_links = minor_tree.xpath('//div[@id="main"]//a//@href')

				for minor2_idx in range(len(minor2_names)):

					# only use names containing "Minor"
		                        if minor2_names[minor2_idx].find("Minor")>0:
		
						minor2_page_url = parent_domain + minor2_links[minor2_idx]
                		                minor2_page = requests.get(minor2_page_url)
		                                minor2_tree = html.fromstring(minor2_page.content)

						minor2_div = minor2_tree.xpath('//div[@id="main"]')

						if first_department_found==0:
							first_department_found = 1
							first_minor_found = 1
							print '<head>'
							print '<title>' + parent_domain + '</title>'	
	
							# css style links	
							minor2_style_links = minor2_tree.xpath('//head/link')
							for minor2_style_link in minor2_style_links:	
								print(etree.tostring(minor2_style_link, pretty_print=True).replace('href="', 'href="' + parent_domain))

							# add page breaks before H1 (program names)
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

							print '</head>'
							print '<body>'

							print '<div id="main"><h1 name="first">' + department_names[department_idx] + '</h1></div>'	
							first_minor_found = 1
	
							print( etree.tostring(minor2_div[0],pretty_print=True).replace('href="', 'href="' + parent_domain).replace('h4','h5').replace('h3','h4').replace('h2','h3').replace('h1','h2') ).replace('<h2>','<h2 name="first">',1)

						else:

							if first_minor_found==0:
								print '<div id="main"><h1>' + department_names[department_idx] + '</h1></div>'	
								first_minor_found = 1
								print( etree.tostring(minor2_div[0],pretty_print=True).replace('href="', 'href="' + parent_domain).replace('h4','h5').replace('h3','h4').replace('h2','h3').replace('h1','h2') ).replace('<h2>','<h2 name="first">',1)
							else:
								print( etree.tostring(minor2_div[0],pretty_print=True).replace('href="', 'href="' + parent_domain).replace('h4','h5').replace('h3','h4').replace('h2','h3').replace('h1','h2') )
# print closing of body and page
print '</body>'
print '</html>'



