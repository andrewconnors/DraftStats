# -*- coding: utf-8 -*-
import scrapy
import time
from pandas import DataFrame, Series


class DraftPositionSpider(scrapy.Spider):
    name = 'draftposition'
    allowed_domains = ['hockey-reference.com']
    years = [x for x in range(1979, 2017)]
    def start_requests(self):
        url = 'http://hockey-reference.com/draft/NHL_'
        for year in self.years:
            yield scrapy.Request(url + str(year) + '_entry.html', meta={'year': year})


    def parse(self, response):
        player_names = response.css('td[data-stat="player"]>a::text').extract()
        overall_ranking = filter(lambda x: x != 'Overall', response.css('th[data-stat="pick_overall"]::text').extract())
        games_played = response.css('td[data-stat="games_played"]::text').extract()
        amateur_team = response.css('td[data-stat="amateur_team"]::text').extract()

        draftdata = {'Year': response.meta['year'], 'Name': Series(player_names), 'Overall Pick': Series(overall_ranking),
        'GP': Series(games_played), 'Amateur Team': Series(amateur_team)}
        hockeydf = DataFrame(draftdata)

        hockeydf.to_csv('./DraftData/draftdata-' + str(response.meta['year']) + '.csv')
        # with open('referenceurls.txt', 'a') as f:
        #     for name in playerNames:
        #         f.write(name + '\n')

        time.sleep(5)
