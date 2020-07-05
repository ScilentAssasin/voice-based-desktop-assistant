# voice-based-desktop-assistant
A simple voice based assistant

This project is made with python-3.x and is tested on ubuntu 20.04

Functions:

The program works for desktop systems; the mode of the program is Voice mode since this program aims at making a voice assistant program.  After the program has been started, the user should have correct voice input “command/request” to make those functions work properly. And this program includes the functions and services of: mail exchange, alarm, location services,  checking weather, Google searching engine, Wikipedia searching engine, telling jokes, News Services, Note Taking and Showing, Wikipedia Search, Answers to General questions and Solve simple mathematics problem via wolfram alpha, open websites, open software installed in the system, help menu etc.. The details below explain how those functions work and different possibilities while facing different commands.

    • Mail exchange, users are able to send the mail to the person with mail address. By giving a correct command contains the mail request keyword together with the destination person; the program will send the mail with the mail address and mail content. This uses SMTP protocol to send the mail.

    • Checking weather, weather service provides the user the weather condition in different city. This service works in the same logic and gives back different result depending on the requested city. The weather service return the current weather condition of the current location.
      
    • Google searching engine, the search engine enable the use to search anything on Google. By detecting the search keyword and search request, the Google search engine will returns the result list displayed in the browser. 

    • Wikipedia searching engine, the search engine enable the use to search anything on Wikipedia. By detecting the search keyword and search request, the Wikipedia search engine will returns the Wikipedia result displayed in the browser. 
      
    • Note Take, user can take notes which are stored in a text file which they can listen to when they need it.
      
    • Application Launch, user can open application installed in the system by telling the software to open it.
      
    • Website open, user can open any website by providing URL for it.(eg. “open facebook.com”).
      
    • Current News,users can listen to current news headlines, provided by the help of google news RSS.
      
    • YouTube, search on youtube and play some videos. this will open browser and play the video.
      
    • Open reddit or subreddits, user can ask system to open reddit or subreddit links.
      
    • Show location on map of anywhere you search.
      
    • Ask simple general questions to the assistant. The answers are answered through wolfram alpha API.
      
    • Solve simple numerical problem via wolfram alpha API.
      
    • Help menu, the help menu provides the user a help list to each function in this program. The user can choose the help menu manually or over the voice if the user doesn’t know how to work with the functions. While the help menu is opened, the help menu gives the examples and explanation of how to work with different functions, the examples clearly show how to work with the function and the user can simply imitate the example to work with different functions.


Requiments:

    •gTTS (Google Text-to-Speech) is a Python library and CLI tool to interface with Google Translates text-to-speech API. This module helps to convert String text to Spoken text and can be saved as .mp3 

    •Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc. Recognizing speech needs audio input, and SpeechRecognition makes it really simple to retrieve this input. Instead of building scripts from scratch to access microphones and process audio files, SpeechRecognition will have you up and running in just a few minutes.

    •PyAudio package is used to access microphone in the system using speech recognition

    •Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

    •WolframAlpha is a computational knowledge engine or answer engine developed by Wolfram Alpha LLC, a subsidiary of Wolfram Research. It is an online service that answers factual queries directly by computing the answer from externally sourced "curated data", rather than providing a list of documents or web pages that might contain the answer as a search engine might. Its API is used by system to ask simple questions and to perform simple calculations

    •Selenium Selenium is an open-source web-based automation tool. Python language is used with Selenium for testing. It has far less verbose and easy to use than any other programming language 

    •webbrowser It module provides a high-level interface to allow displaying Web-based documents to users. Under most circumstances, simply calling the open() function from this module will do the right thing.

    •Beautiful Soup It uses a pluggable XML or HTML parser to parse a (possibly invalid) document into a tree representation. Beautiful Soup provides methods and Pythonic idioms that make it easy to navigate, search, and modify the parse tree.

    •Time This module provides various functions to manipulate time values.

    •Smtplib this supports smtp client class which helps us send email through the assistant.

    •PyOWM it is a client Python wrapper library for OpenWeatherMap web APIs. It allows quick and easy consumption of OWM data from Python applications via a simple object model and in a human-friendly fashion.

    •Subprocess This module allows you to spawn processes, connect to their input/output/error pipes, and obtain their return codes. this is used in many places like calling software installed in the system or passing commands on command line.

Also please create your own api keys.
