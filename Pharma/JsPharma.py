from requests_html import HTMLSession

session = HTMLSession()
URL = 'https://peshawar.infoisinfo.com.pk/card/zaynoon-pharmaceuticals-pvt-ltd/132025'
r = session.get(URL)

r.html.render()
