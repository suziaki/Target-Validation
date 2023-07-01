```python
import scrapy
from web_scraper.items import WebScraperItem

class NcbiSpider(scrapy.Spider):
    name = 'ncbi_spider'
    allowed_domains = ['ncbi.gov']
    start_urls = ['http://www.ncbi.gov/']

    def parse(self, response):
        items = WebScraperItem()

        # Extract specific data from the webpage
        # This is a placeholder and should be replaced with the actual data fields
        items['data_field1'] = response.css('css_selector1::text').extract()
        items['data_field2'] = response.css('css_selector2::text').extract()

        yield items

        # Handle pagination
        next_page = response.css('next_page_css_selector::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```