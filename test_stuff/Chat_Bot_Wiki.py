# wikipedia module
import wikipedia
# speech module
import pyttsx3

def get_speech():
        data =input("Type Something....")
        return data

# def AI_Summarizer(val):
#     summarys= wikipedia.summary(val)
#     return summarys

# def wiki_talk(answer):
#      speech= pyttsx3.init()
#      rate= speech.getProperty('rate')
#      speech.setProperty('rate', rate-10)
#      speech.say('{}'.format(answer))
#      speech.runAndWait()

# Takes from the input from the user from the get speech function.
speech_data = get_speech()

words = speech_data.split(' ')

print(words)

if words[0] == 'search':
    search_word = ''
    for i in range(len(words)):
        if i > 0:
            search_word = search_word + words[i]

    print("Here is what I think about ", search_word)
    print(wikipedia.summary(search_word))

    # val = AI_Summarizer(words[1])
    # wiki_talk(val)



