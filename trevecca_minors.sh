#!/bin/bash

echo "Generating trevecca_minors.html ..."
./trevecca_minors.py > trevecca_minors.html

echo "Generating trevecca_minors_wkhtmltopdf.pdf ..."
wkhtmltopdf --footer-right "[page]" --dump-outline trevecca_minors_wkhtmltopdf_toc.xml trevecca_minors.html trevecca_minors_wkhtmltopdf.pdf

echo "Generating wkhtmltopdf_toc.xsl ..."
wkhtmltopdf --dump-default-toc-xsl > wkhtmltopdf_toc.xsl

echo "Generating trevecca_minors_wkhtmltopdf_toc.html ..."
xsltproc wkhtmltopdf_toc.xsl trevecca_minors_wkhtmltopdf_toc.xml > trevecca_minors_wkhtmltopdf_toc.html

echo "Generating trevecca_minors_wkhtmltopdf_toc.pdf ..."
wkhtmltopdf trevecca_minors_wkhtmltopdf_toc.html trevecca_minors_wkhtmltopdf_toc.pdf

echo "Generating trevecca_minors_wkhtmltopdf_with_TOC.pdf ..."
/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py --output trevecca_minors_wkhtmltopdf_with_TOC.pdf trevecca_minors_wkhtmltopdf_toc.pdf trevecca_minors_wkhtmltopdf.pdf

echo "Done."

