# DraftStats
Playing with some NHL Draft Data to determine correlations

## To Run
In order to run the crawler, navigate to the hockeyreference/hockeyreference file and after running ```pip install```
run ```scrapy crawl draftposition```

## Project Goals
Ideally, once all the data is collected, I would like to run the relevant pieces of data through an ANN to determine draft value for an individual player. I will determine draft value by looking at careers of established NHL players and their junior numbers and by applying a statistic called "Average Value" used in the nfl (https://www.pro-football-reference.com/blog/index37a8.html) I will tryu and predict the average value for new players coming into the league. This ideally will then be used in a web application for the public to use as another tool to needlessly bug Kyle Dubas about decisions he makes regarding the Leafs. (Sorry Kyle, I like what you're doing, hopefully this helps)

## Disclaimer
After 2 years of letting this sit and gaining experience in other places, I am collecting the data I need throug the nhl stats api. When my NHLData project is finished NHL-Data-Analysis is finished, that will likely be the source of information for this project
