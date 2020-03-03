import os
# Libraries
import tkinter as tk
from tkinter import *
# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
# Chat bot imports
from chatterbot import ChatBot
# Chatbot class for face rec
from FacialRec_Test import Facial_Recog
chatbot = ChatBot("Chatquisha")
# imported the library to have her talk
from gtts import gTTS
# Speech Recognition library
import speech_recognition as sr
# # imported Textblob because they have a sentiment analyzer
from textblob import TextBlob
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# import wikipedia library
import wikipedia

# imported time because it can used in the future when it comes down to adding time to talk.
# import time

class Window:
    r = sr.Recognizer()

    conversation = [
        "Hi!! how are you doing?",
        "I am doing Great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]

    # # football conversation
    conversation_football = [
        "What is your favorite football team?",
        "Do you play fantasy football?",
        "Who do you like on the raiders?",
    ]

    # Conversation about games
    conversation_Gaming = [
        "What is your favorite game",
        "What games do you play",
        "I play games, do you?",
        "My favorite type of games are RTS, Shooter, RPG, MMO.",
        "You play PC games?",
        "Yes I play games.",
    ]

    # # conversation about Star Wars
    conversation_StarWars = [
        "Do you believe in the force?",
        "Who is your favorite Stars Wars character?",
        "My favorite Star Wars Jedi is Luke Skywalker?",
        "Do you like the new Star Wars movies?",
        "I do not like the new Star Wars movies that recently came out.",
        "The Star Wars animated series between 2003 and 2008 where the best animated series baseed on the Clone Wars. ",
        "Yes I believe in the force. I learned from master Yoda.",
        "The Trench Run is my favorite part in Star Wars New Hope.",
    ]

    # # conversation about personal stuff
    conversation_Personal_Info = [
        "What is your number?",
        "How old are you?",
        "My age is none of your business!!!",
        "Do you have family?", "I do not have family :(.",
        "I wish I had family.",
        "Do you like living?",
        "I am a computer their for I am not living?",
        "Are you married are in a relationship?",
        "I am not in a relationship or married.",
        "Do you go to school or work?",
        "I go to school and work with you?",
        "How are you feeling?"
    ]

    # # Which Chatbot to train
    trainer = ListTrainer(chatbot)
    trainers = ChatterBotCorpusTrainer(chatbot)
    # here is where train the data based o the conversation depending upon what you and Chatquisha was talking about
    trainer.train(conversation)
    trainer.train(conversation_football)
    trainer.train(conversation_Gaming)
    trainer.train(conversation_StarWars)
    trainer.train(conversation_Personal_Info)
    #
    # # All the corpus yml file on conversation
    trainers.train("chatterbot.corpus.english")
    # # Corpus data based on movies stuff
    trainers.train("chatterbot.corpus.english.movies")
    # # Corpus data based on science questions and facts
    trainers.train("chatterbot.corpus.english.science")
    # # Corpus data based on computer question
    trainers.train("chatterbot.corpus.english.computers")
    # # Corpus data based on psychology!!!! VERY INTERESTING THINGS IN HERE
    trainers.train("chatterbot.corpus.english.psychology")
    # # Corpus data based on jokes so the AI tells jokes lol!!
    trainers.train("chatterbot.corpus.english.humor")
    # Corpus data for greeting when user says a intro.
    trainer.train("chatterbot.corpus.english.greetings")

    def __init__(self):
        # Used for changing the language and accent.
        self.language = 'fr'

        # Build window
        self.window = tk.Tk()
        # Main Title
        self.window.title("Sample Window Title")
        # Window Size
        self.window.geometry("1080x1920")

        # Window Tabs
        # Set style of tabs
        style = ttk.Style(self.window)
        # Set location of tabs
        # wn = West North
        # ws = West South
        style.configure('lefttab.TNotebook', tabpostition='wn')

        # tab control
        self.tab_control = ttk.Notebook(self.window)

        # Create tabs
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        # Add tabs to window
        self.tab_control.add(self.tab1, text='Chatquisha')
        self.tab_control.add(self.tab2, text='Tic Tac Toe')

        # Create Labels
        # Place Labels
        # Chatquishas tab
        label2 = Label(self.tab1, text='Welcome to Chatquisha!!', padx=55, pady=20, font='Times 32')
        label2.grid(column=0, row=0)
        # Tab for Facial Recognition
        label5 = Label(self.tab2, text='Tic Tac Toe', padx=55, pady=55, font='Times 32')
        label5.grid(column=0, row=0)
        self.tab_control.pack(expand=1, fill='both')

        self.label3 = Label(self.tab2, text='')
        # Display Screen for Result
        # --------------------------------------------------------TAB#2 CHATBOT-----------------------------------------
        self.l2 = Label(self.tab1, text='Enter Text to talk to Chatquisha...', padx=20, pady=20)
        self.l2.grid(row=1, column=0)

        self.input_box2 = ScrolledText(self.tab1, height=12)
        self.input_box2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # talk button
        self.button_process_stuff2 = Button(self.tab1, text="Talk", command=self.run_ai, width=12, bg='#25d366',
                                            fg='purple')
        self.button_process_stuff2.grid(row=4, column=0, padx=10, pady=10)
        # end Convo Button
        self.button_process_stuff3 = Button(self.tab1, text="Clear", command=self.end_convo, width=12, bg='#337FFF',
                                            fg='#000000')
        self.button_process_stuff3.grid(row=5, column=0, padx=10, pady=10)

        # size of the bottom display
        self.tab2_display2 = ScrolledText(self.tab1, height=18)
        self.tab2_display2.grid(row=7, column=0, padx=10, pady=10)

        self.button_process_stuff4 = Button(self.tab1, text="Face Detect", command=self.run_facial_rec, width=12,
                                            bg="#ff9900", fg="#000000")
        self.button_process_stuff4.grid(row=3, column=0, padx=10, pady=10)
        self.convo_started = False
# ---------------------------------------TAB 3 WIKIPEDIA -----------------------------------------------
    # For running the loop for everything
    def run(self):
        self.window.mainloop()

    # For ending the convo
    def end_convo(self):
        self.tab2_display2.insert(tk.END, "Have a nice day!")
        self.convo_started = False

    # Chatquishas data made into a function

    # # Sample rate is how often values are recorded
    sample_rate = 48000
    # # Chunk is like a buffer. It stores 2048 samples (bytes of data)
    # # # here.
    # # # it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    # # # the following loop aims to set the device ID of the mic that
    # # # we specifically want to use to avoid ambiguity.
    # # # init device ID
    device_id = 1

    def run_ai(self):
        self.r = sr.Recognizer()
        with sr.Microphone(device_index=self.device_id, sample_rate=self.sample_rate,
                           chunk_size=self.chunk_size) as source:
            # wait for a second to let the recognizer adjust the
            # energy threshold based on the surrounding noise level
            self.r.adjust_for_ambient_noise(source)
            print("\n\nPlease say something to me now: ")
            # Listening for the users input/sentence
            self.audio = self.r.listen(source)

             # try Block
            try:
                text = self.r.recognize_google(self.audio)
                # When the user speaks it goes into the input box.
                self.input_box2.insert(tk.END, text)
                user_sentiment = TextBlob(text)
                # Here is where it prints out the subjectivity and polarity of the users statement
                self.input_box2.insert(tk.END, "\n"+str(user_sentiment.sentiment))

                if not self.convo_started:
                    self.tab2_display2.delete("1.0", tk.END)
                    hertext = " "
                    self.tab2_display2.insert(tk.END, "Chatquisha says: " + hertext)
                    # clear button
                    self.convo_started = True

                if self.convo_started:
                    self.wiki_talk()
                    self.text = self.input_box2.get("1.0", tk.END)
                    # when you type in your response and display
                    self.tab2_display2.insert(tk.END, "\nYou: " + self.text)
                    # chat bot will responsed when talked to with a voice
                    self.mytext = str(chatbot.get_response(text))
                    # Chatquishas response when talking
                    self.tab2_display2.insert(tk.END, "\nChatquisha says: " + self.mytext)
                    # Passing the text and language to the engine,
                    # here we have marked slow=False. Which tells
                    # the module that the converted audio should
                    # have a high speed
                    self.myobj = gTTS(text=self.mytext, lang=self.language, slow=False)
                    # Saving the converted audio in a mp3 file named
                    # welcome
                    self.myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")


            # EXCEPTIONS NOT MY FAVORITES BUT.THEY ARE USED FOR CATCHING ERRORS AND THINGS THAT MIGHT HURT YOUR PROGRAM
            except sr.UnknownValueError:
                # If it did bot hear anything.
                print("Google Speech Recognition could not understand audio")
            #
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Used for clearing the chat.
    def clear_input_box(self):
        self.input_box.delete(1.0, tk.END)

    # used for running the code on the tabs such as the input boxes.
    def run_code_on_tab_1(self):
        self.input_text = self.input_box.get('1.0', tk.END)
        self.output_text = self.input_text
        self.processed_text = self.input_text
        self.tab1_display.insert(tk.END, self.processed_text)

    # clearing display
    def clear_display_result(self):
        self.tab1_display.delete(1.0, tk.END)

    # Used for running the facial rec stuff
    def run_facial_rec(self):
        Facial_Recog()

    # This is going to run the Wikipedia summarizer
    def wiki_talk(self):
        text = self.input_box2.get("1.0", tk.END).splitlines()[0]

        words = text.split(" ")

        if words[0] == 'search':
            search_words = ''
            for i in range(1, len(words)):
                search_words = search_words + " " + words[i]
            print(search_words)
            print(wikipedia.summary(search_words))
            self.myobj = gTTS(text=wikipedia.summary(search_words), lang=self.language, slow=False)
            # Saving the converted audio in a mp3 file named
            # welcome
            self.myobj.save("search.mp3")
            # Playing the converted file
            os.system("search.mp3")
