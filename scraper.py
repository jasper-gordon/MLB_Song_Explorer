#File to handle web scraping of MLB game data using Beautiful Soup to convert to a csv file

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
import csv
import json


class Scraper():

    def __init__(self, name, season):
        self.name = name
        self.season = season
        self.url = ''
        self.player_dict = {}
        self.first_name, self.last_name = self.name.split()
        self.file_name = self.last_name + "_stats.csv"
        
        self.load_dict()
        self.create_url()
        self.scrape()

        
    def create_url(self):
        '''
        if len(self.last) > 4:
            self.url = 'https://www.baseball-reference.com/players/gl.fcgi?id=' + self.last[:5] + self.first[0:2] + '02&t=b&year=' + self.season
        else:
            self.url = 'https://www.baseball-reference.com/players/gl.fcgi?id=' + self.last + self.first[0:2] + '02&t=b&year=' + self.season
        '''
        self.url = 'https://www.baseball-reference.com/players/gl.fcgi?id=' + self.player_dict[self.name] + '&t=b&year=' + str(self.season)
    
    def scrape(self):
        
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        #Find header row
        header = soup.find('thead')
        #Find column names from header row
        columns = [col.get_text() for col in header.find_all('th')]
        columns.pop(0) #Get rid of unneeded rank column 
        #Creating an empty dataframe with column names from the header 
        final_df = pd.DataFrame(columns=columns)
        #Grabbing game data
        games =  soup.find_all('tr', attrs={'id':re.compile('batting_gamelogs.')})
        for game in games:
            #get stats for each game
            stats = [stat.get_text() for stat in game.find_all("td")]
            #Create a dataframe for the single game's stats
            temp_df = pd.DataFrame(stats).transpose()
            temp_df.columns = columns
            #Join the single player's stats with the overall dataset
            final_df = pd.concat([final_df, temp_df], ignore_index=True)
        final_df.to_csv(self.file_name , index = False, sep=',', encoding='utf-8')

    def get_file(self):
        return self.file_name

    #Scrapes every player name and id from Baseball Reference and saves in a list as tuple
    def name_scrape(self):
        for letter in ascii_lowercase: #Loops through every letter in alphabet to find every player
            url = "https://www.baseball-reference.com/players/" + letter + "/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            players = soup.select('#div_players_  p a')
            for tag in players:
                self.player_dict[tag.text] = self.get_id(tag['href'])
    
    def get_id(self, link):
        return re.findall("(?<=/[a-zA-Z]/)(.*?)(?=\.)", link)[0]

    def to_file(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.player_dict, fp)

    def load_dict(self):
        with open('players.json') as file:
            self.player_dict = json.load(file)

    def practice_scrape(self):
        page = requests.get("https://www.baseball-reference.com/players/w/")
        soup = BeautifulSoup(page.text, 'html.parser')
        #Find the correct player link
        name = 'Matt Wagner'
        link = (soup.find("a", href = True, text = name))

