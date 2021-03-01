import requests

r = requests.get('http://172.18.58.238/')

print("Status code:")
print("\t *", r.status_code)

h = requests.head('http://172.18.58.238/')
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

#Scrapy code after this

import scrapy

class ProjectSpider(scrapy.Spider):
    name = "Project"

    start_urls = [
        'http://172.18.58.238/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
        }
# Unit Testing code

import unittest

class TestMyProgram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()






