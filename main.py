# Importing chatterbot and Chatterbot.trainers
# Importing ListTrainer and nltk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk

# Download the punkt tokenizer
nltk.download('punkt')

chatbot = ChatBot('Oswald the Lucky PlannerBot')

# Create object of ChatBot class with Storage Adapter
chatbot = ChatBot(
    'Oswald the Lucky PlannerBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create object of ChatBot class with Logic Adapter
chatbot = ChatBot(
    'Oswald the Lucky PlannerBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(chatbot)

user_input = input("Enter Your Name: ")
print("Hi there! I'm Oswald the Lucky PlannerBot, how can I help?")
while True:
    request=input(user_input+':')
    if request =='thank you' or request=='Thank you':
        print('PlannerBot: No problem, cya real soon!')
        break
    else:
        response=chatbot.get_response(request)
        print('PlannerBot:', response)


class Parks:
    """
        A class representing the Parks at Disney World.
        """

prompt1 = 'Magic Kingdom'
prompt2 = 'Hollywood Studios'
prompt3 = 'EPCOT'
prompt4 = 'Animal Kingdom'

while True:
    if trainer.train =='Magic Kingdom':
        print(prompt1)
    elif trainer.train == 'Hollywood Studios':
        print(prompt2)
    elif trainer.train == 'EPCOT':
        print(prompt3)
    else:
        print(prompt4)


trainer.train([
"Hi",
"Hi there! I'm Oswald the Lucky PlannerBot, how can I help?",
"I'm going to Disney World soon. What are the best rides at Magic Kingdom?",
"Here are my favorites: are Space Mountain, TRON Lightcycle Run, Pirates of the Caribbean, Tiana's Bayou Adventure, Big Thunder Mountain RailRoad and Buzz Lightyear's Space Ranger Spin!",
"Thank you",
"No problem! Cya real soon!"
])

trainer.train([
"Hi",
"Hey! I'm Oswald the Lucky PlannerBot, how can I help?",
"I'm going to Disney World soon. What are the best rides at Hollywood Studios?",
"Here are my favorites: Mickey & Minnie's Runaway Railway, Millennium Falcon: Smuggler's Run, Slinky Dog Dash, Rock 'n' Roller Coaster Starring Aerosmith, Star Tours - The Adventures Continue, Star Wars: Rise of the Resistence, Toy Story Mania! and The Twilight Zone Tower of Terror!",
"Thank you",
"No problem! Cya real soon!"
])

trainer.train([
"Hi",
"Hi there! I'm Oswald the Lucky PlannerBot, how can I help?",
"I'm going to Disney World soon. What are the best rides at EPCOT?",
"Here are my favorites: Guardians of the Galaxy: Cosmic Rewind, Living with the Land, Remy's Ratatouille Adventure, The Seas with Nemo and Friends, Test Track and Soarin' Around the World!",
"Thank you"
"No problem! Cya real soon!"
])

trainer.train([
"Hi",
"Hey! I'm Oswald the Lucky PlannerBot, how can I help?",
"I'm going to Disney World soon. What are the best rides at Animal Kingdom?",
"That's my favorite park actually. Here are my favorite rides there: Avatar Flight of Passage, Kilimanjaro Safaris, Na'vi River Journey, DINOSAUR, Expedition Everest - Legend of the Forbidden Mountain and Kali River Rapids!"
"Thank you"
"No problem! Cya real soon!"
])
