import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt//']

    def parse(self, response):
        
        countries = response.xpath("//tbody[@class='jsx-2642336383']/tr")
        for country in countries:
            yield {
                'country_name' : country.xpath(".//td[1]/a/text()").get(),
                'gdp_debt' : country.xpath(".//td[2]/text()").get()
                }
            