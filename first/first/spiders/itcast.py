import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itheima.com/teacher.html#ajavaee"]

    def parse(self, response):
        node_list = response.xpath('//div[@class = "li_txt"]')
        for node in node_list:
            temp = {}
            temp['name'] = node.xpath("./h3/text()")[0].extract()
            temp['title'] = node.xpath("./h4/text()")[0].extract()
            temp['desc'] = node.xpath("./p/text()")[0].extract()
            yield temp


