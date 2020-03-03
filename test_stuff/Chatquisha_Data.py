# import os
# # Libraries
# import tkinter as tk
# from tkinter import *
# # Window Tabs Libraries
# from tkinter import ttk
# from tkinter.scrolledtext import *
# # Chat bot imports
# from chatterbot import ChatBot
#
# import Facial_Rec
#
# chatbot = ChatBot("Chatquisha")
# # imported the library to have her talk
# from gtts import gTTS
# # Speech Recognition library
# import speech_recognition as sr
#
# # # imported Textblob because they have a sentiment analyzer
# from textblob import TextBlob
#
# from chatterbot.trainers import ListTrainer
#
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
#
#
#
# class Window:
#     r = sr.Recognizer()
#
#     def __init__(self):
#         # Build window
#         self.window = tk.Tk()
#         # Main Title
#         self.window.title("Sample Window Title")
#         # Window Size
#         self.window.geometry("680x800")
#
#         # Window Tabs
#         # Set style of tabs
#         style = ttk.Style(self.window)
#         # Set location of tabs
#         # wn = West North
#         # ws = West South
#         style.configure('lefttab.TNotebook', tabpostition='wn')
#
#         # tab control
#         self.tab_control = ttk.Notebook(self.window)
#
#         # Create tabs
#         self.tab1 = ttk.Frame(self.tab_control)
#         self.tab2 = ttk.Frame(self.tab_control)
#         # self.tab3 = ttk.Frame(self.tab_control)
#         # self.tab4 = ttk.Frame(self.tab_control)
#         self.tab5 = ttk.Frame(self.tab_control)
#
#         # Add tabs to window
#         self.tab_control.add(self.tab1, text='Home tab')
#         self.tab_control.add(self.tab2, text='Chatquisha')
#         # self.tab_control.add(self.tab3, text='Another tab')
#         # self.tab_control.add(self.tab4, text='Another tab')
#         self.tab_control.add(self.tab5, text='About tab')
#
#         # Create Labels
#         # Place Labels
#         label1 = Label(self.tab1, text='Home', padx=5, pady=5)
#         # 0,0 is top left of window
#         label1.grid(column=0, row=0)
#         # Chatquishas tab
#         label2 = Label(self.tab2, text='Welcome to Chatquisha!!', padx=55, pady=20, font="Times 32")
#         label2.grid(column=0, row=0)
#         # other tab
#         # label3 = Label(self.tab3, text='My Page Title', padx=5, pady=5)
#         # label3.grid(column=0, row=0)
#         # # another tab
#         # label4 = Label(self.tab4, text='My Page Title', padx=5, pady=5)
#         # label4.grid(column=0, row=0)
#         # another tab
#         label5 = Label(self.tab5, text='About Title', padx=5, pady=5)
#         label5.grid(column=0, row=0)
#
#         self.tab_control.pack(expand=1, fill='both')
#
#         # Main Home Tab
#         l1 = Label(self.tab1, text='Enter Text to Process ...', padx=20, pady=20)
#         l1.grid(row=1, column=0)
#         self.input_box = ScrolledText(self.tab1, height=10)
#         self.input_box.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
#
#         # Button
#         self.button_reset_input = Button(self.tab1, text='Reset Input', command=self.clear_input_box, width=12, bg='purple', fg='#fff')
#         self.button_reset_input.grid(row=3, column=0, padx=10, pady=10)
#
#         self.button_process_stuff = Button(self.tab1, text="Run me", command=self.run_code_on_tab_1, width=12, bg='#25d366',
#                                            fg='purple')
#         self.button_process_stuff.grid(row=4, column=0, padx=10, pady=10)
#
#         self.button_clear_output = Button(self.tab1, text='Clear Output', command=self.clear_display_result, width=12, bg='purple',
#                                      fg='#fff')
#         self.button_clear_output.grid(row=5, column=0, padx=10, pady=10)
#
#         # Display Screen for Result
#         self.tab1_display = ScrolledText(self.tab1)
#         self.tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
#         # --------------------------------------------------------TAB#2 CHATBOT------------------------------------------------
#         self.l2 = Label(self.tab2, text='Enter Text to talk to Chatquisha..', padx=20, pady=20)
#         self.l2.grid(row=1, column=0)
#
#         self.input_box2 = ScrolledText(self.tab2, height=12)
#         self.input_box2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
#
#         # talk button
#         self.button_process_stuff2 = Button(self.tab2, text="Talk", command=self.run_ai, width=12, bg='#25d366', fg='purple')
#         self.button_process_stuff2.grid(row=4, column=0, padx=10, pady=10)
#         # end Convo Button
#         self.button_process_stuff3 = Button(self.tab2, text="Clear", command=self.end_convo, width=12, bg='#337FFF', fg='#000000')
#         self.button_process_stuff3.grid(row=5, column=0, padx=10, pady=10)
#
#         # size of the bottom display
#         self.tab2_display2 = ScrolledText(self.tab2, height=18)
#         self.tab2_display2.grid(row=7, column=0, padx=10, pady=10)
#
#         self.convo_started = False
#
#     def run(self):
#         self.window.mainloop()
#
#     def end_convo(self):
#
#         self.tab2_display2.insert(tk.END, "Have a nice day!")
#         self.convo_started = False
#
#     def convo_data(self):
#
#         # starter conversation
#         conversation = ["Hi!! how are you doing?",
#                         "I am doing Great.",
#                         "That is good to hear",
#                         "Thank you.",
#                         "You're welcome."
#                         ]
#         # # football conversation
#         conversation_football = ["What is your favorite football team?",
#                                  "Do you play fantasy football?",
#                                  "Who do you like on the raiders?",
#                                  ]
#
#         # Conversation about games
#         conversation_Gaming = ["What is your favorite game",
#                                "What games do you play",
#                                "I play games, do you?",
#                                "The type of games I play are RTS, Shooter, RPG, MMO.",
#                                "You play PC games?",
#                                "Yes I play games.",
#                                ]
#
#         # # conversation about Star Wars
#         conversation_StarWars = ["Do you believe in the force?",
#                                  "Who is your favorite Stars Wars character?",
#                                  "My favorite Star Wars Jedi is Luke Skywalker?",
#                                  "Do you like the new Star Wars movies?",
#                                  "I do not like the new Star Wars movies that recently came out.",
#                                  "The Star Wars animated series between 2003 and 2008 where the best animated series baseed on the Clone Wars. ",
#                                  "Yes I believe in the force. I learned from master Yoda.",
#                                  "The Trench Run is my favorite part in Star Wars New Hope.",
#                                  ]
#
#         # # conversation about personal stuff
#         conversation_Personal_Info = ["What is your number?",
#                                       "How old are you?",
#                                       "My age is none of your business!!!",
#                                       "Do you have family?", "I do not have family :(.",
#                                       "I wish I had family.",
#                                       "Do you like living?",
#                                       "I am a computer their for I am not living?",
#                                       "Are you married are in a relationship?",
#                                       "I am not in a relationship or married.",
#                                       "Do you go to school or work?",
#                                       "I go to school and work with you?",
#                                       "How are you feeling?"
#                                       ]
#
#         # # Which Chatbot to train
#         trainer = ListTrainer(chatbot)
#         trainers = ChatterBotCorpusTrainer(chatbot)
#         # # here is how we train the data based on the conversation depending upon what you and Chatquisha was talking about
#         trainer.train(conversation)
#         trainer.train(conversation_football)
#         trainer.train(conversation_Gaming)
#         trainer.train(conversation_StarWars)
#         trainer.train(conversation_Personal_Info)
#         #
#         # # All the corpus yml file on conversation
#         trainers.train("chatterbot.corpus.english")
#         # # Corpus data based on movies stuff
#         trainers.train("chatterbot.corpus.english.movies")
#         # # Corpus data based on science questions and facts
#         trainers.train("chatterbot.corpus.english.science")
#         # # Corpus data based on computer question
#         trainers.train("chatterbot.corpus.english.computers")
#         # # Corpus data based on psychology!!!! VERY INTERESTING THINGS IN HERE
#         trainers.train("chatterbot.corpus.english.psychology")
#         # # Corpus data based on jokes so the AI tells jokes lol!!
#         trainers.train("chatterbot.corpus.english.humor")
#
#     # # Sample rate is how often values are recorded
#     sample_rate = 48000
#     # # Chunk is like a buffer. It stores 2048 samples (bytes of data)
#     # # # here.
#     # # # it is advisable to use powers of 2 such as 1024 or 2048
#     chunk_size = 2048
#     # # # the following loop aims to set the device ID of the mic that
#     # # # we specifically want to use to avoid ambiguity.
#     # # # init device ID
#     device_id = 1
#
#     def run_ai(self):
#         self.r = sr.Recognizer()
#         with sr.Microphone(device_index=self.device_id, sample_rate=self.sample_rate,
#                                 chunk_size=self.chunk_size) as source:
#             # wait for a second to let the recognizer adjust the
#             # energy threshold based on the surrounding noise level
#             self.r.adjust_for_ambient_noise(source)
#             print("\n\nPlease say something to me now:")
#             # Listening for the users input/sentence
#             self.audio = self.r.listen(source)
#
#             #         # try Block
#             try:
#                 text = self.r.recognize_google(self.audio)
#                 # When the user speaks it goes into the input box.
#                 self.input_box2.insert(tk.END, "\nYou: " + text)
#                 user_sentiment = TextBlob(text)
#                 # Here is where it prints out the subjectivity and polarity of the users statement
#                 self.input_box2.insert(tk.END, user_sentiment.sentiment)
#
#                 if not self.convo_started:
#                     self.tab2_display2.delete("1.0", tk.END)
#                     self.tab2_display2.insert(tk.END, "\n\n\t*** Welcome to a talk with Chatquisha ***\n")
#                     hertext = "\nHello, I am Chatquisha "
#                     self.tab2_display2.insert(tk.END, "Chatquisha says: " + hertext)
#                     # clear button
#                     self.convo_started = True
#                 if self.convo_started:
#                     self.text = self.input_box2.get("1.0", tk.END)
#                     # when you type in your response and display
#                     self.tab2_display2.insert(tk.END, "\nYou: " + text)
#                     # chat bot will responsed when talked to with a voice
#                     self.mytext = str(chatbot.get_response(text))
#                     # chatquishas response when talking
#                     self.tab2_display2.insert(tk.END, "\nChatquisha says: " + self.mytext)
#                     self.language = 'en'
#
#                     #                 # Passing the text and language to the engine,
#                     #                 # here we have marked slow=False. Which tells
#                     #                 # the module that the converted audio should
#                     #                 # have a high speed
#                     self.myobj = gTTS(text=self.mytext, lang=self.language, slow=False)
#                     #
#                     #                 # Saving the converted audio in a mp3 file named
#                     #                 # welcome
#                     self.myobj.save("welcome.mp3")
#                     #
#                     #                 # Playing the converted file
#                     os.system("welcome.mp3")
#             #
#             # EXCEPTIONS NOT MY FAVORITES BUT.... THEY ARE USED FOR CATCHING ERRORS AND THINGS THAT MIGHT HURT YOUR PROGRAM
#             except sr.UnknownValueError:
#                 #
#                 print("Google Speech Recognition could not understand audio")
#             #
#             except sr.RequestError as e:
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
#
#
#     def clear_input_box(self):
#         self.input_box.delete(1.0, tk.END)
#
#     def run_code_on_tab_1(self):
#         self.input_text = self.input_box.get('1.0', tk.END)
#         self.output_text = self.input_text
#         self.processed_text = self.input_text
#         self.tab1_display.insert(tk.END, self.processed_text)
#
#     def clear_display_result(self):
#         self.tab1_display.delete(1.0, tk.END)
#
#     def run_facial_rec(self):
#         Facial_Rec.facial_rec()