# -*- coding: utf-8 -*-
import scrapy
from pandas import Series, DataFrame


class EurolegueSpider(scrapy.Spider):
    name = 'euroleague'
    allowed_domains = ['www.eurohockey.com']
    years = [x for x in range(1979, 2017)]
    def start_requests(self):
        for year in self.years:
            url = 'http://www.eurohockey.com/stats/league/' + str(year) + '/124-nla.html?season='+ str(year) +'&type=1&position=0&nationality=0'
            yield scrapy.Request(url, meta={'year': year})

    def parse(self, response):
        #parsing logic
        player_names = response.css('.player>a::text').extract()
        games_played = response.css('tr:nth-child(4)::text').extract()
        goals=  response.css('table tr:nth-child(5)::text').extract()
        assists = response.css('tr:nth-child(6)::text').extract()
        points = response.css('tr:nth-child(7)::text').extract()

        draftdata = {'Year': response.meta['year'], 'Name': Series(player_names), 'Goals': Series(goals),
        'GP': Series(games_played), 'Assists': Series(assists), 'Points': Series(points)}

        hockeydf = DataFrame(draftdata)
        hockeydf.to_csv('./EuroData/eurostats-' + str(response.meta['year']) + '.csv')

        time.sleep(20)
