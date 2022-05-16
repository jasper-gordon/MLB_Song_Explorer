10 December 2021
MLB PLAYER PLAYER PROJECT

Goal: To translate any given hitting season for any given MLB player into a musical piece in an effort
to represent the highs, lows, and ebs and flows of a major leage season in a creative fasion using the power
of music and hopefully animation.

Compontents:
1. Web scraping player data
2. Repackaging data, converting it into "musical notes"
3. Create a music system to play a given "song"
4. A driver module that handles user input and orchestrates these tasks 

TO RUN SITE:
1. Open terminal
2. Cd to project folder
3. input: http-server
    ^This will launce the local server so you can view the site
4. Click on the link or go to: http://127.0.0.1:8080/
5. Enjoy!

TO TEST MUSIC PLAYER:
1. Run driver.py 
2. Follow prompts

Tasks to Complete:
1. Scrape all player names and ID's from baseball reference instead of singular scrape
2. Build a name spell checker to handle mispelled names
3. Configure fast API


https://www.baseball-reference.com/players/gl.fcgi?id=PerezSa02&t=b&year=2015 Basic page
https://www.baseball-reference.com/players/gl.fcgi?id=perezsa02&t=b&year=2015 Game log page
https://www.baseball-reference.com/players/gl.fcgi?id=aokino0102&t=b&year=2016
https://www.baseball-reference.com/players/gl.fcgi?id=aokino01&t=b&year=2016

https://www.baseball-reference.com/players/gl.fcgi?id=wadety01&t=b&year=2020



<a href="/players/gl.fcgi?id=wadety01&amp;t=b&amp;year=2017">2017</a>
<a href="/players/gl.fcgi?id=wadety01&amp;t=b&amp;year=2018">2018</a>
<a href="/players/gl.fcgi?id=wadety01&amp;t=f&amp;year=2017">2017</a>


Credits:
http://norvig.com/spell-correct.html for Spell Correction