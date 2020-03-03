# Libraries
import tkinter as tk
from tkinter import *
# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot

chatbot = ChatBot("Chatquisha")


class text_to_text:
    # starter conversation
    conversation = ["Hi!! how are you doing?",
                    "I am doing Great.",
                    "That is good to hear",
                    "Thank you.",
                    "You're welcome."
                    ]
    # football conversation
    conversation_football = ["What is your favorite football team?",
                             "My favorite football team is the Oakland Raiders.",
                             "Do you play fantasy football?",
                             "Who do you like on the raiders?",
                             ]

    # Conversation about games
    conversation_Gaming = ["What is your favorite game",
                           "What games do you play",
                           "I play games, do you?",
                           "The type of games I play are RTS, Shooter, RPG, MMO.",
                           "You play PC games?",
                           "Yes I play games.",
                           ]

    # conversation about Star Wars
    conversation_StarWars = ["Do you believe in the force",
                             "Who is your favorite character.",
                             "My favorite Jedi is Luke Skywalker.",
                             "Do you like the new Star Wars movies?",
                             "I do not like the new Star Wars movies that recently came out."
                             ]

    # conversation about personal stuff
    conversation_Personal_Info = ["What is your number?",
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

    # Which Chatbot to train
    trainer = ListTrainer(chatbot)
    # here is how we train the data based on the conversation depending upon what you and Chatquisha was talking about
    trainer.train(conversation)
    trainer.train(conversation_football)
    trainer.train(conversation_Gaming)
    trainer.train(conversation_StarWars)

    def __int__(self):
        # Create GUI
        # Create Window
        # Build main window

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
        self.tab_control.add(self.tab1, text='Home tab')
        self.tab_control.add(self.tab2, text='Chatquisha')
        # Create Labels
        # Place Labels
        self.label1 = Label(self.tab1, text='Home', padx=5, pady=5)
        # 0,0 is top left of window
        self.label1.grid(column=0, row=0)
    # Chatquishas tab
        self.label2 = Label(self.tab2, text='Welcome to Chatquisha!!', padx=55, pady=20, font="Times 32")
        self.label2.grid(column=0, row=0)
    # other tab
        self.label3 = Label(self.tab3, text='My Page Title', padx=5, pady=5)
        self.label3.grid(column=0, row=0)
    # another tab
        self.label4 = Label(self.tab4, text='My Page Title', padx=5, pady=5)
        self.label4.grid(column=0, row=0)
    # another tab
        self.label5 = Label(self.tab5, text='About Title', padx=5, pady=5)
        self.label5.grid(column=0, row=0)

        self.tab_control.pack(expand=1, fill='both')

    # Functions
    def run_code_on_tab_1(self):
        self.input_text = self.input_box.get('1.0', tk.END)
        output_text = self.input_text
        self.processed_text = self.input_text
        self.tab1_display.insert(tk.END, self.processed_text)

    def clear_input_box(self):
        self.input_box.delete(1.0, END)

    def clear_display_result(self):
        self.tab1_display.delete(1.0, END)


    # this is for the clear but to stop talking about the subject you and the AI are talking about.
    convo_started = False

    # is technically how get the response and everything to work
    def run_ai(self):
        global convo_started
        if not convo_started:
            self.tab2_display2.delete("1.0", tk.END)
            self.tab2_display2.insert(tk.END, "\n\n\t*** Welcome to a talk with Chatquisha ***\n")
            self.chatbot_response = ("\nHello, I am Chatquisha ")
            self.tab2_display2.insert(tk.END, "Chatquisha says: " + self.chatbot_response)
        # clear button
        convo_started = True
        if convo_started:
            self.user_response = self.input_box2.get("1.0", tk.END)
            # when you type in your response and display
            self.tab2_display2.insert(tk.END, "\nYou: " + self.user_response)
            self.chatbot_response = str(self.chatbot.get_response(self.user_response))
            # chatquishas response when talking
            self.tab2_display2.insert(tk.END, "\nChatquisha says: " + self.chatbot_response)

    # when you end the conversation your on she will display have a "nice day"
    def end_convo(self):
        global convo_started

        self.tab2_display2.insert(tk.END, "Have a nice day!")
        self.convo_started = False

        # Main Home Tab
        self.l1 = Label(self.tab1,
                        text ='Enter Text to Process in some way. but delete what you said before to continue the convo',
                        padx=20, pady=20)
        self.l1.grid(row=1, column=0)
        self.input_box = ScrolledText(self.tab1, height=10)
        self.input_box.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Button
        self.button_reset_input = Button(self.tab1, text='Reset Input', command=self.clear_input_box, width=12,
                                         bg='purple', fg='#fff')
        self.button_reset_input.grid(row=3, column=0, padx=10, pady=10)

        self.button_process_stuff = Button(self.tab1, text="Run me", command=self.run_code_on_tab_1, width=12,
                                           bg='#25d366', fg='purple')
        self.button_process_stuff.grid(row=4, column=0, padx=10, pady=10)

        self.button_clear_output = Button(self.tab1, text='Clear Output', command=self.clear_display_result, width=12,
                                          bg='purple', fg='#fff')
        self.button_clear_output.grid(row=5, column=0, padx=10, pady=10)

        # Display Screen for Result
        self.tab1_display = self.ScrolledText(self.tab1)
        self.tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
        # --------------------------------------------------------TAB#2 CHATBOT---------------------------------------------------------------
        self.l2 = self.Label(self.tab2, text='Enter Text to talk to Chatquisha..', padx=20, pady=20)
        self.l2.grid(row=1, column=0)

        self.input_box2 = self.ScrolledText(self.tab2, height=12)
        self.input_box2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def run_code_on_tab_2(self):
        #  input output function
        self.input_text2 = self.input_box2.get('1.0', tk.END)
        self.output_text2 = self.input_text2
        self.processed_text2 = self.input_text2
        self.tab2.insert(tk.END, self.processed_text2)

        # talk button
        self.button_process_stuff2 = Button(self.tab2, text="Talk", command=self.run_ai, width=12, bg='#25d366', fg='purple')
        self.button_process_stuff2.grid(row=4, column=0, padx=10, pady=10)
        # end Convo Button
        self.button_process_stuff3 = Button(self.tab2, text="Clear", command=self.end_convo, width=12, bg='#337FFF', fg='#000000')
        self.button_process_stuff3.grid(row=5, column=0, padx=10, pady=10)

        # size of the bottom display
        self.tab2_display2 = ScrolledText(self.tab2, height=18)
        self.tab2_display2.grid(row=7, column=0, padx=10, pady=10)

    # Keep window alive