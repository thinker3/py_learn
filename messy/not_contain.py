from scrapy.selector import HtmlXPathSelector

text = '''\
<table>
  <tbody>
    <tr>
      <td>Black</td>
      <td><strong>Specifications</strong></td>
    </tr>

    <tr>
      <td>Finish Specifications</td>
      <td>Black</td>
    </tr>

    <tr>
      Specifications
      <td>Action</td>
      <td>Semi-Automatic</td>
    </tr>

    <tr a='Specifications'>
      <td>Caliber</td>
      <td>7.62mmX39mm</td>
    </tr>
  </tbody>
</table>'''

hxs = HtmlXPathSelector(text=text)
#trs = hxs.select('//table/tbody/tr[not(contains(td, "Specifications"))]') # wrong
#trs = hxs.select('//table/tbody/tr[not(contains(.|./@*, "Specifications"))]') # wrong
trs = hxs.select('//table/tbody/tr[not(.//text()|./@*[contains(., "Specifications")])]')
trs = hxs.select('//table/tbody/tr[not(.//text() or ./@*[contains(., "Specifications")])]')
for one in trs.extract():
    print(one)
