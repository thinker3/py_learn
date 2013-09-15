from scrapy.selector import HtmlXPathSelector

text = '''\
<table>
  <tbody>
    <tr>
      <td>
        <strong>Specifications</strong>
      </td>
    </tr>
    <tr>
      <td>Finish Specifications</td>
      <td>Black</td>
    </tr>
    <tr>
      <td>Action</td>
      <td>Semi-Automatic</td>
    </tr>
    <tr>
      <td>Caliber</td>
      <td>7.62mmX39mm</td>
    </tr>
  </tbody>
</table>'''

hxs = HtmlXPathSelector(text=text)
#trs = hxs.select('//table/tbody/tr[not(contains(td, "Specifications"))]')
#trs = hxs.select('//table/tbody/tr[not(contains(., "Specifications"))]')
trs = hxs.select('//table/tbody/tr[not(contains(./td/strong, "Specifications"))]')
for one in trs.extract():
    print one
