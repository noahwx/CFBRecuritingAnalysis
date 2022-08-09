# College Football Recruitment Ranking Analysis

### Analysis of on3 College Football Recruiting Data
#### Analysis of ten years worth of on3 college football recruiting data of the top fifty teams in college. From the data, I wanted to find what teams were successful at recruiting and what teams that are not. For college football recruiting, recruiting the best players (five stars) is what every team strives for. However, it does not discredit nor prove that a specific five-star rated player is what is needed for a particular team. I learned much about different teams throughout this project, and I hope you can also.

### How did I start this project?
#### To begin this project all that was needed was a python webscrapper, a url, and some crucial python librarys. To build the webscrapper I used these libraries BeautifuSoup4, Requests, csv, datetime, pandas, os, urllib and pathlib. All eight of theses lobrares help me to achieve my first goal of this project. 

### Goals of the Project
#### Build my expertise in data analysis, webscrapping with python and building dashboards.

## Objective #1
#### The first objective I had for this project was to have the ability to simply take the url of the on3 rankings (https://www.on3.com/db/rankings/consensus-team/football/2023/), and extract a teams ranking, team name, amount of five, four, and three star players recruited, a teams total commits, a teams average rating, avgerage NIL (Name, Iamge and Likeness) spent by teams, and a teams on3 score.

![image](https://user-images.githubusercontent.com/47571584/183323271-c23ce898-9fc7-491f-8a51-9e67cd3a53b9.png)

### How is the webscrapper built?
#### The first goal of the webscraper is to get input from the user of what does the user want to do. To acheive this I included a menu at the start of the python program. The menu asks the user to select either input #1 to go to the on3 Webscrapper, input #2 for insturctions on how the webscrapper works, and finally input #3 to exit the program. 

### Selecting Input #1:
#### If a user selects the first input, the user is then prompt to paste or enter the on3 Ranking page url (https://www.on3.com/db/rankings/consensus-team/football/2023/). 

![image](https://user-images.githubusercontent.com/47571584/183332062-f9dcafbb-2f22-46fa-9cae-42548ceda0d0.png)

#### After the user inputs the url, the webscrapper script begins the process of breaking the rankings chart down and then storing the data as a csv.

            url = input('Paste the url:')
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')
            chart = soup.find('ol')

            today = datetime.date.today()

            data = []

            year = PurePosixPath(
                unquote(
                 urlparse(
                        url
                    ).path
                 )
            ).parts[5]

            for item in chart :
                data.append({
                    'date_w_accessed' : today,
                    'date_ranked' : year,
                    'ranking' : item.find(class_='MuiTypography-root MuiTypography-h6 MuiTypography-colorTextPrimary').text,
                    'team_name' : item.find(class_='MuiTypography-root MuiLink-root MuiLink-underlineHover TeamRow_teamName__BlGjp MuiTypography-h5 MuiTypography-colorPrimary').text,
                    'five_stars' : item.find(class_ ='TeamRow_fiveStars__DoclT').find('p').text,
                    'four_stars' : item.find(class_='TeamRow_fourStars__zj4TO').find('p').text,
                    'three_stars' : item.find(class_='TeamRow_threeStars__i7Ce1').find('p').text,
                    'total_commits' : item.find(class_='TeamRow_totalCommits__mvaKY').find('p').text,
                    'avg_rating' : item.find(class_='TeamRow_averageRating__PYZLM').find(class_='MuiTypography-root TeamRow_txtRating__OJ510 MuiTypography-subtitle1 MuiTypography-colorTextPrimary').text,
                    'avg_nil' : item.find(class_='TeamRow_averageNil__tZQs0').find(class_='MuiTypography-root TeamRow_txtRating__OJ510 MuiTypography-subtitle1 MuiTypography-colorTextPrimary').text,
                    'on3_score' : item.find(class_='TeamRow_score__upKOD').find('p').text
                })

##### First real problem: 
##### The first problem that I faced when making the webscrapper was ensuring that when I scrapped a ranking chart for a year not 2023. To complete this I used the pathlib library to accomplish this. Specfically, from pathlib I imported PurePosixPath to parse the url to extract the text of the end of the url "2023".

#### To get the data for the next ten years. I just changed the date at the end of the url ("/2023") to ("/2013").  

# Objective #2
#### So I got the data, so now what?
### After getting the data for the past ten years, and having the files saved to csv files. I then opened a jupyter notebook and began the process of cleaing, analyzing and interpreting the data at hand.

## First Step:
#### The first step I took in the notebook was to import the necessary libraries I needed. The libraries I used in the notebook included pandas, glob, os, pathlib, seaborn and matplotlib. 

## Second Step:
#### The second step I took was to combine the 10 csv's into one csv, and then read the combined csv into a dataframe for use with pandas. To combine the 10 csv's together I first set a varible named "path" to the file path of the dataset folder from the webscrapper, next the glob library was used to combine files and lastly I outputed the glob data to a variable named "file". I then created the dataframe variable called "dfs". After this I created a for loop to set the vairable "file" to "f", read the combined file to pandas as a "data", used the .stem method from pathlib to get the filename without the extension, next I appended the data to the dataframe "dfs". And, finally I used the concatenate object from pandas to concatenate the "dfs" dataframe, and set the dataframe to "df".  
![image](https://user-images.githubusercontent.com/47571584/183333321-ec880625-524d-4bd9-bf96-fb535d337640.png)

## Third Step:
#### The third step I took was to clean the dataframe to fit what I needed for the project. 

#### The first step I took when cleaing the data was to sort the 'date_ranked', and 'ranking' columns in ascending order. After sorting the data, I then dropped the 'date_w_accessed', and the 'file' columns.  
![image](https://user-images.githubusercontent.com/47571584/183333516-38b044d7-c447-41bb-a7c0-67c761f55655.png)
#### The second step I took in cleaning the data was to replace the "-", "$", "K" to "0", "", "", double quatations is to set the dollar sign ("$") and "K" to nothing. After replacing the strings I then set the type og the 'avg_nil' to a float.
![image](https://user-images.githubusercontent.com/47571584/183333584-7f2ce479-d8a1-4e8c-8699-f46dad0a47d5.png)

## Fourth Step:
#### The fourth step I took was to began the process of analyzing the data at hand. To start I used the describe object of pandas to learn about some of the statistical informaton of the data. To start I answered a few questions I wanted to answer.
 
## Questions
### Question #1: Which Team has the most commits during a recruiting period in the past 10 years?
#### South Carolina

### Question #2: Which Team has the most commits on average during a recruiting period in the past 10 years?
#### Kansas

### Question #3 Which Team has the most commits in the past 10 years?
#### Georgia

### Question #4 Which Team has the least commits in the past 10 years?
#### Northern Iowa

### Question #5 Which Team has the most five star recruits for the past 10 years?
#### Alabama

### Question #6 Which Teams have the least five star recurits for the past 10 years?
#### Georgia Tech, Washington State, Northwestern, Wake Forest, Kansas, Oregon State, Utah, Northern Iowa, Purdue, Boston College, UCF, Texas Tech, Cincinnati, Iowa State

### Question #7 Which team has the highest on3 score?
#### Alabama

### Question #8 Which team has the lowest on3 score?
#### Northern Iowa

### Question #9 What is Oregon State's on3 Score for the past 10 years?
#### 85.283

## After these questions, I wanted to look deeper into the data by breaking it down into the respective conferences of each school, the state the school is in and teams that have won a national championship.
