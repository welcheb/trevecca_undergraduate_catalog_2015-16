#!/bin/bash

echo "Generating trevecca.html ..."
./trevecca.py > trevecca.html

echo "Generating trevecca_wkhtmltopdf.pdf ..."
wkhtmltopdf --footer-right "[page]" --dump-outline trevecca_wkhtmltopdf_toc.xml trevecca.html trevecca_wkhtmltopdf.pdf

echo "Generating wkhtmltopdf_toc.xsl ..."
wkhtmltopdf --dump-default-toc-xsl > wkhtmltopdf_toc.xsl

echo "Generating trevecca_wkhtmltopdf_toc.html ..."
xsltproc wkhtmltopdf_toc.xsl trevecca_wkhtmltopdf_toc.xml > trevecca_wkhtmltopdf_toc.html

echo "Generating trevecca_wkhtmltopdf_toc.pdf ..."
wkhtmltopdf trevecca_wkhtmltopdf_toc.html trevecca_wkhtmltopdf_toc.pdf

echo "Generating trevecca_wkhtmltopdf_with_TOC.pdf ..."
/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py --output trevecca_wkhtmltopdf_with_TOC.pdf trevecca_wkhtmltopdf_toc.pdf trevecca_wkhtmltopdf.pdf

echo "Done."

