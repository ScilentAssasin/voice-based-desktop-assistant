import datetime
import random
import re
import smtplib
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import webbrowser

import bs4
import requests
import speech_recognition as sr
import wolframalpha
from bs4 import BeautifulSoup as soup
from gtts import gTTS
from pygame import mixer
from pyowm import OWM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def talk(audio):
    # speaks audio passed as argument

    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang="en")
        text_to_speech.save("audio.mp3")
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()


def myCommand():
    "listens for commands"
    # Initialize the recognizer
    # The primary purpose of a Recognizer instance is, of course, to recognize speech.
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("red queen is Ready...")
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        # listens for the user's input
        audio = r.listen(source)
        print("analyzing...")

    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")
        time.sleep(2)

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print("Your last command couldn't be heard")
        command = myCommand()

    return command


def search_google(cmd):
    reg_ex = re.search("open google and search (.*)", cmd)
    search_for = cmd.split("search", 1)[1]
    print("you asked to search for : ", end='')
    print(search_for)
    url = "https://www.google.com/"
    if reg_ex:
        subgoogle = reg_ex.group(1)
        url = url + 'r/' + subgoogle
    talk("Okay!")
    driver = webdriver.Firefox(executable_path="/home/abcd/geckodriver")  # add geckodriver executabe path
    driver.get("http://www.google.com")
    search = driver.find_element_by_name("q")
    search.send_keys(str(search_for))
    search.send_keys(Keys.RETURN)  # hit return after you enter search text


def reddit(cmd):
    reg_ex = re.search('open reddit (.*)', cmd)
    url = 'https://www.reddit.com/'
    if reg_ex:
        subreddit = reg_ex.group(1)
        url = url + 'r/' + subreddit
    webbrowser.open(url)
    talk('The Reddit content has been opened for you Sir.')


def open_site(cmd):
    reg_ex = re.search('open (.+)', cmd)
    if reg_ex:
        domain = reg_ex.group(1)
        print(domain)
        url = 'https://www.' + domain
        webbrowser.open(url)
        talk('The website you have requested has been opened for you Sir.')
    else:
        pass


def email():
    talk("What is the subject?")
    time.sleep(3)
    subject = myCommand()
    talk("What should I say?")
    message = myCommand()
    content = "Subject: {}\n\n{}".format(subject, message)

    # init gmail SMTP
    mail = smtplib.SMTP("smtp.gmail.com", 587)

    # identify to server
    mail.ehlo()

    # encrypt session
    mail.starttls()

    # login
    mail.login("username_gmail", "password_gmail")  # add username and password

    # send message
    mail.sendmail("FROM", "TO", content)

    # end mail connection
    mail.close()

    talk("Email sent.")


def joke():
    res = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept": "application/json"})
    if res.status_code == requests.codes['ok']:
        talk(str(res.json()['joke']))
    else:
        talk('oops!I ran out of jokes')


def wikipedia(cmd):
    reg_ex = re.search("wikipedia (.+)", cmd)
    if reg_ex:
        query = cmd.split("wikipedia", 1)[1]
        response = requests.get("https://en.wikipedia.org/wiki/" + query)
        if response is not None:
            html = bs4.BeautifulSoup(response.text, "html.parser")
            title = html.select("#firstHeading")[0].text
            paragraphs = html.select("p")
            for para in paragraphs:
                print(para.text)
            intro = "\n".join([para.text for para in paragraphs[0:3]])
            print(intro)
            mp3name = "speech.mp3"
            language = "en"
            myobj = gTTS(text=intro, lang=language, slow=False)
            myobj.save(mp3name)
            mixer.init()
            mixer.music.load("speech.mp3")
            mixer.music.play()


def write_note():
    talk("What should i write, sir")
    note = myCommand()
    file = open('RQ.txt', 'w')
    talk("Sir, Should i include date and time")
    snfm = myCommand()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)


def show_note():
    talk("Showing Notes")
    file = open("RQ.txt", "r")
    print(file.read())
    talk(file.read(6))


def youtube(cmd):
    reg_ex = re.search("youtube (.+)", cmd)
    if reg_ex:
        domain = cmd.split("youtube", 1)[1]
        query_string = urllib.parse.urlencode({"search_query": domain})
        html_content = urllib.request.urlopen(
            "http://www.youtube.com/results?" + query_string
        )
        search_results = re.findall(
            r'href="\/watch\?v=(.11})', html_content.read().decode()
        )
        # print("http://www.youtube.com/watch?v=" + search_results[0])
        webbrowser.open(
            "http://www.youtube.com/watch?v={}".format(search_results[0])
        )
        pass

def weather(cmd):
    city = cmd.split("in", 1)[1]
    owm = OWM(API_key='')  # create your own owm key
    obs = owm.weather_at_place(city)
    w = obs.get_weather()
    k = w.get_status()
    x = w.get_temperature(unit='celsius')
    talk(
        'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
            city, k, x['temp_max'], x['temp_min']))
    time.sleep(3)


def news():
    news_url = "https://news.google.com/news/rss"
    Client = requests.get(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    for news in news_list[:15]:
        talk(news.title.text.encode('utf-8'))


def launch(cmd):
    reg_ex = re.search('launch (.*)', cmd)
    if reg_ex:
        appname = reg_ex.group(1)
        subprocess.call(appname)
        talk('I have launched the desired application')


def wolfram(cmd):
    reg_ex = re.search('me (.*)', cmd)
    app_id = ''  # create your own wolfrom aplha key
    client = wolframalpha.Client(app_id)
    if reg_ex:
        ques = reg_ex.group(1)
        res = client.query(ques)
        talk(next(res.results).text)


def maps(cmd):
    reg_ex = re.search('where is (.*)', cmd)
    if reg_ex:
        loc = reg_ex.group(1)
        talk("User asked to Locate")
        talk(loc)
        webbrowser.open("https://www.google.com/maps/search/" + loc + "/")

def red_queen(command):
    errors = ["I don't know what you mean", "Excuse me?", "Can you repeat it please?"]

    if "help" in command:
        print('''You can use these commands and I'll help you out:
              1. open google and search **** : search in google.
              2. open reddit : opens the reddit.
              3. Open reddit *subreddit* : Opens the subreddit.
              4. open *website name*.com : opens the website.
              5. Send E-Mail : Follow up questions such as recipient name, content will be asked in order.
              6. tell a joke : Tells you a joke.
              7. Can you search in wikipedia *topic* : searches wikipedia for the topic and answers you.
              8. Search in youtube *video name* : opens the video in the browser.
              9. weather in *city* : tells about the current weather in city.
              10. News for today : top stories from google news.
              11. current time : tells about current time.
              12. red queen tell me *genral question* : serches on wolfrom alpha and gives out answer. 
              13. where is *location* : serches and opens google maps for location.
              14. Stop : to stop whatever red queen is talking about. 
              15. bye bye : quit the program.

              ''')

    # Search on Google
    elif 'open google and search' in command:
        search_google(command)

    # open subreddit Reddit
    elif 'open reddit' in command:
        reddit(command)

    # open <website name>
    elif 'open' in command:
        open_site(command)

    # Send Email
    elif 'email' in command:
        email()

    # joke
    elif 'joke' in command:
       joke()

    # search in wikipedia (e.g. Can you search in wikipedia apples)
    elif 'wikipedia' in command:
        wikipedia(command)

    # stop
    elif 'stop' in command:
        mixer.music.stop()

    # write note
    elif "write a note" in command:
        write_note()
    
    # read note
    elif "show note" in command:
        show_note()

        # Search videos on Youtube and play (e.g. Search in youtube believer)
    elif 'youtube' in command:
        youtube(command)

    # time
    elif 'time' in command:
        now = datetime.datetime.now()
        talk('Current time is %d hours %d minutes' % (now.hour, now.minute))
        time.sleep(3)

    #  weather forecast in your city (e.g. weather in Bhopal)
    elif 'weather in' in command:
        weather(command)

    # top stories from google news
    elif 'news for today' in command:
        news()

    # launch any application
    elif 'launch' in command:
        launch(command)

    # ask general questions
    elif 'red queen tell me' in command:
        wolfram(command)

    # finds location in google maps
    elif 'where is' in command:
        maps(command)
        
    
    elif 'hello' in command:
        talk("Hello! I am red queen. How can I help you?")
        time.sleep(3)
    elif 'who are you' in command:
        talk("I am a state-of-the-art supercomputer developed by Umbrella Corporation")
        time.sleep(3)
    elif 'reason for you' in command:
        talk("I was created to help Suveer Singhai in a Minor project ")
        time.sleep(3)
    elif 'is love' in command:
        talk("It is 7th sense that destroy all other senses")
        time.sleep(3)
    elif 'quit' in command:
        talk("See you Again!")
        time.sleep(3)
        sys.exit(0)
    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(3)


talk("red queen activated!")

# loop to continue executing multiple commands
while True:
    time.sleep(4)
    red_queen(myCommand())
   
      
