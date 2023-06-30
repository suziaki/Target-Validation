```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from web_scraper.spiders.ncbi_spider import NcbiSpider
from web_scraper import data_processing
from web_scraper import pytorch_model

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(NcbiSpider)
    process.start() 

    data = data_processing.process_data()
    model = pytorch_model.train_model(data)

if __name__ == "__main__":
    main()
```