# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml
from pandas import Series, DataFrame

session = requests.Session()
ahlurl = 'https://theahl.com/stats/player-stats/all-teams/'

page = 1
years = [x for x in [1,8,12,16,30,34,37,40,43,48,51,54,57]]

for year in years:
    params = {
    'playertype': 'skater',
    'position': 'skaters',
    'rookie': 'no',
    'sort': 'points',
    'statstype': 'standard',
    'page': page,
    'league': 4
    }
    html = session.get(ahlurl + str(year), params=params).text
    parsePage(html)

def parsePage(html):
    while True:
        #parsing logic
        soup = BeautifulSoup(html, "lxml")
        pageNext = soup.find(class_='ht-paging-buttons').children[1]
        if(pageNext.has_attr('class'))
        player_names = response.css('.player>a::text').extract()
        games_played = response.css('tr:nth-child(4)::text').extract()
        goals=  response.css('table tr:nth-child(5)::text').extract()
        assists = response.css('tr:nth-child(6)::text').extract()
        points = response.css('tr:nth-child(7)::text').extract()

        draftdata = {'Year': response.meta['year'], 'Name': Series(player_names), 'Goals': Series(goals),
        'GP': Series(games_played), 'Assists': Series(assists), 'Points': Series(points)}

        hockeydf = DataFrame(draftdata)
        hockeydf.to_csv('./EuroData/eurostats-' + str(response.meta['year']) + '.csv')
        page += 1
        time.sleep(20)
