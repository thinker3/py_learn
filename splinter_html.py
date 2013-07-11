from splinter import Browser
import time

def get_qqs_html(qqs):
    html = qqs.html
    if not html:
        time.sleep(1)
        return get_qqs_html(qqs)
    else:
        return html
url = 'http://www.dzsc.com/stock-ic/AD51_025.html'
firefox= Browser()
firefox.visit(url)
firefox.check('checkbox')
qqs = firefox.find_by_id('qqmsn1')
if qqs:
    qqs = qqs[0]
    print dir(qqs)
    print
    html = get_qqs_html(qqs)
    print html

html = firefox.html
html = html.encode('gb18030')
f = open('_splinter.html', 'w')
f.write(html)
f.close()
firefox.quit()
