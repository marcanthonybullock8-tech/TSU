#!/usr/bin/env python3
"""Convert TSU markdown docs (canon bibles, scripts) to matching PDFs.

Setup (once):
    python3 -m venv .venv
    .venv/bin/pip install markdown xhtml2pdf reportlab

Usage:
    .venv/bin/python3 tools/md2pdf.py canon/*.md scripts/*.md README.md

Each <name>.md produces a sibling <name>.pdf. Re-run after any edit to a
tracked .md file to keep its PDF in sync - PDFs are the deliverable format
going forward, but the .md files remain the editable source of truth.
"""
import sys, os
import markdown
from xhtml2pdf import pisa

CSS = """
<style>
@page {
    size: letter;
    margin: 0.85in 0.85in 0.85in 0.85in;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.4;
    color: #1a1a1a;
}
h1 {
    font-size: 19pt;
    margin-top: 0pt;
    margin-bottom: 4pt;
    color: #111111;
}
h2 {
    font-size: 14pt;
    margin-top: 16pt;
    margin-bottom: 6pt;
    color: #111111;
    border-bottom: 0.75pt solid #999999;
    padding-bottom: 3pt;
}
h3 {
    font-size: 11.5pt;
    margin-top: 12pt;
    margin-bottom: 4pt;
    color: #111111;
}
p {
    margin-top: 0pt;
    margin-bottom: 8pt;
    text-align: left;
}
hr {
    background-color: #bbbbbb;
    height: 1pt;
    margin: 12pt 0pt;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 12pt;
    font-size: 8.5pt;
}
th, td {
    border: 0.75pt solid #999999;
    padding: 4pt 6pt;
    text-align: left;
    vertical-align: top;
}
th {
    background-color: #e6e6e6;
    font-weight: bold;
}
code {
    font-family: Courier, monospace;
    background-color: #f2f2f2;
    font-size: 9.5pt;
}
pre {
    font-family: Courier, monospace;
    font-size: 9pt;
    line-height: 1.2;
    white-space: pre-wrap;
    background-color: #fafafa;
    border: 0.5pt solid #dddddd;
    padding: 10pt;
    margin: 10pt 0pt;
}
pre code {
    background-color: transparent;
}
strong { font-weight: bold; }
em { font-style: italic; }
ul, ol {
    margin-top: 0pt;
    margin-bottom: 8pt;
    padding-left: 16pt;
}
li {
    margin-bottom: 3pt;
}
a { color: #1a4fa0; }
</style>
"""

def convert(md_path):
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    html_body = markdown.markdown(
        text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"]
    )
    html = "<html><head><meta charset='utf-8'>" + CSS + "</head><body>" + html_body + "</body></html>"
    with open(pdf_path, "wb") as out:
        result = pisa.CreatePDF(html, dest=out)
    status = "ERROR" if result.err else "OK"
    print(status + ": " + md_path + " -> " + pdf_path)
    return not result.err

if __name__ == "__main__":
    ok = True
    for md_path in sys.argv[1:]:
        ok = convert(md_path) and ok
    sys.exit(0 if ok else 1)
