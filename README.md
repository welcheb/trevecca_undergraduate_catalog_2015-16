# trevecca_undergraduate_catalog_2015-16
Python script to generate HTML of Trevecca Undergraduate Catalog 2015-16

## Run `trevecca.sh` to execute all steps below or execute commands one at a time
~~~~
./trevecca.sh
~~~~

## Run `trevecca.py` to generate `trevecca.html`
~~~~
./trevecca.py > trevecca.html
~~~~

## Options for trevecca.html
1. Open in a web browser
2. Open in MS Word and optionally add page numbers and a Table of Contents, e.g., `trevecca.doc`
3. Print from web browser or MS Word to PDF, e.g., `trevecca_Firefox.pdf`, `trevecca_MSWord.pdf`
4. Use with `wkhtmltopdf` (see below)

## Features of PDF generated by `wkhtmltopdf`
1. Clickable hyperlinks
2. Table of Contents sidebar
3. Background colors
4. Table of Contents preface (optional)

## Steps to use `wkhtmltopdf`
1. Download and install static version of `wkhtmltopdf` from [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html)

2. Execute `wkhtmltopdf` to generate `trevecca_wkhtmltopdf.pdf` (TOC is saved to an .xml file)

	~~~~
wkhtmltopdf --footer-right "[page]" --dump-outline trevecca_wkhtmltopdf_toc.xml trevecca.html trevecca_wkhtmltopdf.pdf
	~~~~

3. Dump `wkhtmltopdf` TOC XSL style sheet

	~~~~
wkhtmltopdf --dump-default-toc-xsl > wkhtmltopdf_toc.xsl
	~~~~
	
4. Transform `trevecca_wkhtmltopdf_toc.xml` to `trevecca_wkhtmltopdf_toc.html` with `xsltproc`

	~~~~
xsltproc wkhtmltopdf_toc.xsl trevecca_wkhtmltopdf_toc.xml > trevecca_wkhtmltopdf_toc.html 
	~~~~
	
5. Convert trevecca_wkhtmltopdf_toc.html to PDF

	~~~~
wkhtmltopdf trevecca_wkhtmltopdf_toc.html trevecca_wkhtmltopdf_toc.pdf
	~~~~

6. Combine PDF files, e.g. on Mac OS X

	~~~~
/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py --output trevecca_wkhtmltopdf_with_TOC.pdf trevecca_wkhtmltopdf_toc.pdf trevecca_wkhtmltopdf.pdf
	~~~~


