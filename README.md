# CFBRecuritingAnalysis

### Analysis of on3 College Football Recruiting Data
#### Analysis of ten years worth of on3 college football recruiting data of the top 50 teams. From the data I wanted to find what teams were succesfull at recruiting and what teams that are not. When it comes to college football recruiting, recruiting the best players(five stars) or the players who are not viewed by sport journalist as being the cream of the crop when it comes to recruits. I learned a lot about different teams throughout this project and I hope that you can also.

### How did I start this project?
#### To begin this project all that was needed was a python webscrapper, a url, and some crucial python librarys. To build the webscrapper I used these libraries BeautifuSoup4, Requests, csv, datetime, pandas, os, urllib and pathlib. All eight of theses lobrares help me to achieve my first goal of this project. 

## Objective #1
#### The first objective I had for this project was to have the ability to simply take the url of the on3 rankings (https://www.on3.com/db/rankings/consensus-team/football/2023/), and extract a teams ranking, team name, amount of five, four, and three star players recruited, a teams total commits, a teams average rating, avgerage NIL (Name, Iamge and Likeness) spent by teams, and a teams on3 score.

##### First real problem: 
##### The first problem that I faced when making the webscrapper was ensuring that when I scrapped a ranking chart for a year not 2023. To complete this I used the pathlib library to accomplish this. Specfically, from pathlib I imported PurePosixPath to parse the url to extract the text of the end of the url "2023".
![image](https://user-images.githubusercontent.com/47571584/183323271-c23ce898-9fc7-491f-8a51-9e67cd3a53b9.png)
