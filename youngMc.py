from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)