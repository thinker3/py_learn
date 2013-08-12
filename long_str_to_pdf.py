from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, cm


doc = SimpleDocTemplate("wrap.pdf")
styles = getSampleStyleSheet()
style = styles["Normal"]
Story = []

bogustext = '''
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3). It is completely written in pure Python so it is platform independent.
'''
p = Paragraph(bogustext, style)
Story.append(p)
Story.append(Spacer(2*inch, 2*cm)) # width, height. height is more important.

long_line = '''
Build the document from a list of flowables. If the filename argument is provided then that filename is used rather than the one provided upon initialization. If the canvasmaker argument is provided then it will be used instead of the default. For example a slideshow might use an alternate canvas which places 6 slides on a page (by doing translations, scalings and redefining the page break operations).
'''
p = Paragraph(long_line, style)
Story.append(p)

doc.build(Story)


