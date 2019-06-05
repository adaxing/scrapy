import scrapy

# scrapy.Spider 
# define initial request, how to follow links in the pages
class QuotesSpider(scrapy.Spider):
    # used for scrapy crawl name, identifical
    name = "quotes"

    # can be replaced by 
    # start_urls = [
    #   'http://quotes.toscrape.com/page/1/',
    #   'http://quotes.toscrape.com/page/2/'
    # ]
    # since parse() is Scrapy default callback method, can be called without explicitly assigned callback
    def start_requests(self):
        urls = [
            'https://adaxing.github.io/archives/cs61b-4/#more',
        ]
        # when scrapy from website and callback func
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # handle to parse the downloaded page content to extract data
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'blog-%s.html' %page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

