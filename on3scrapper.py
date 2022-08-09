from bs4 import BeautifulSoup
import requests
import csv
import datetime as datetime
import pandas as pd
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
import os

if __name__=='__main__':
    print('on3 Scrapper')

def main():
    mylist = []
    while True:
        operation = input('''
Select operation:
[1] on3 
[2] Instructions
[3] Exit program
''')
        if operation == '1':
            url = input('Paste the url: ')
            page = requests.get(url)

            path = input('Paste the path to the dataset folder: ')

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

            outfile = os.path.join(path, f'{year}_on3.csv')

            df = pd.DataFrame(data)
            df.to_csv(outfile, index=False)
            print('Webpage scraped sucessfully!\n')

        elif operation == '2':
            print("Instructions\n")
            print('Create a folder named dataset.\nCopy the url from on3 CFB Recruiting Rankings webpage.\nIn the scrapper, select the [1] option.\nPaste the on3 rankings url.\nCopy the filepath that was created earlier.\nPaste the file path next.\nThe program will run and save the scrapped file to the path pasted.')
            continue

        elif operation == '3':
            break

        else:
            print("Invalid choice. Please try again.")

main()
