#File that acts as the controller for the entire system. Asks for user input, retrieves data, analyzes it, repackages,
#and presents it with music and eventually animation

#Get input from user

from music_player import Music_Player
from scraper import Scraper
from csv_reader import *

def prompt_user():
    print ("Welcome to the MLB Song Explorer. Which player would you like to explore?")
    player_name = input("Enter first and last name seperated by a space: ")
    season = input( "Which season would you like to analyze? ")
    sc = Scraper(player_name, season)
    file_name = sc.get_file()
    musical_score = to_song(file_name)
    print ("Here is the musical score: ", musical_score)
    player = Music_Player(musical_score)
    player.play_song()
prompt_user()