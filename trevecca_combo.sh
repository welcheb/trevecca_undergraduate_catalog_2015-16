#!/bin/bash

echo "Generating trevecca_combo.html ..."
./trevecca_combo.py > trevecca_combo.html

echo "Generating trevecca_combo_wkhtmltopdf.pdf ..."
wkhtmltopdf --footer-right "[page]" --dump-outline trevecca_combo_wkhtmltopdf_toc.xml trevecca_combo.html trevecca_combo_wkhtmltopdf.pdf

echo "Generating wkhtmltopdf_toc.xsl ..."
wkhtmltopdf --dump-default-toc-xsl > wkhtmltopdf_toc.xsl

echo "Generating trevecca_combo_wkhtmltopdf_toc.html ..."
xsltproc wkhtmltopdf_toc.xsl trevecca_combo_wkhtmltopdf_toc.xml > trevecca_combo_wkhtmltopdf_toc.html

echo "Generating trevecca_combo_wkhtmltopdf_toc.pdf ..."
wkhtmltopdf trevecca_combo_wkhtmltopdf_toc.html trevecca_combo_wkhtmltopdf_toc.pdf

echo "Generating trevecca_combo_wkhtmltopdf_with_TOC.pdf ..."
/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py --output trevecca_combo_wkhtmltopdf_with_TOC.pdf trevecca_combo_wkhtmltopdf_toc.pdf trevecca_combo_wkhtmltopdf.pdf

echo "Done."

