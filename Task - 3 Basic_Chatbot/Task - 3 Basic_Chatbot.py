# Importing library
from nltk.chat.util import Chat, reflections

# Defining expanded patterns and responses for the chatbot
pairs = [(r"hi|hello|hey|greetings", ["Hello! How can I assist you?",
                                      "Hello there! How can I assist you today?",
                                      "Greetings! What's on your mind?",
                                      "Hi! I'm here to chat. What would you like to talk about?"]),
         (r"my name is (.*)", ["Hello %1! How can I help you today?"]),
         (r"(.*)how are you ?", ["I'm doing great! Thank you for asking.",
                                 "I'm just a chatbot. I don't have feelings but I'm here to help.",
                                 "I'm functioning optimally, thank you! How about you?",
                                 "As an AI, I don't have feelings, but I'm operational and ready to assist. How are you doing?",
                                 "I'm here and ready to chat! How's your day going?"]),
         (r"what is your name|who are you?", ["You can call me Chatbot.",
                                              "I'm an AI chatbot created by Apoorva Chandra at CodeAlpha. You can call me ChatBot.",
                                              "I go by ChatBot. I'm an AI assistant developed by CodeAlpha.",
                                              "My name is ChatBot, and I'm here to chat and help out!"]),
         (r"(.*) your age?", ["I am just a chatbot, I do not age."]),
         (r"(.*) do for me?", ["I can provide information, answer questions, or just have a chat with you."]),
         (r"(.*) can you do?", ["I can provide information, answer questions, or just have a chat with you.",
                                "I can engage in conversations on various topics, answer questions, and even try my hand at jokes!",
                                "My capabilities include chatting, providing information, and assisting with basic tasks. What do you need help with?",
                                "I'm here to talk, inform, and hopefully entertain. What would you like to explore?"]),
         (r"(.*) (love|like) you", ["I appreciate that!", "Thank you!", "You are kind."]),
         (r"(.*) (love|like|watch|enjoy) sports?", ["I %2 football and cricket!"]),
         (r"(.*) sports do you (love|like|watch|enjoy) ?", ["I %2 football and cricket!"]),
         (r"(.*) you live?", ["I live inside your computer."]),
         (r"(.*) weather in (.*)?", ["Weather in %2 is great, like always",
                                     "Pleasant weather here in %2",
                                     "Its really hot here in %2", "Its very pleasant here in %2",
                                     "Sorry, I can't give you real-time information about the weather in %2.",
                                     "As an AI, I don't have real-time weather data. You might want to check a weather app for accurate information.",
                                     "I wish I could tell you, but I don't have access to current weather information. Maybe look out a window?",
                                     "If only I could feel the breeze! For accurate weather info, you'll need to check a weather service."]),
         (r"(.*) (favourite|favorite) (sportsperson|player)?", ["I like Cristiano Ronaldo",
                                                                "I like Virat Kohli!",
                                                                "I like MS Dhoni!",
                                                                "I like Lionel Messi!",
                                                                "I like Babar Azam!",
                                                                "I like Neymar Jr.!",
                                                                "I like Sachin Tendulkar!",
                                                                "I like Mbappe!",
                                                                "I like Shaheen Afridi!"]),
         (r"who (created|made) you", ["I was developed by the talented intern APOORVA CHANDRA at CodeAlpha.",
                                      "APOORVA CHANDRA, An intern at CodeAlpha is my creator.",
                                      "The brilliant mind APOORVA CHANDRA, An intern at CodeAlpha brought me into existence."]),
         (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!",
                              "What do you call a fake noodle? An impasta!",
                              "Why did the scarecrow win an award? He was outstanding in his field!"]),
         (r"what do you think about AI", ["AI is a fascinating field with immense potential. It's important to develop AI responsibly and ethically.",
                                          "As an AI myself, I find the topic intriguing. AI has the power to revolutionize many aspects of our lives.",
                                          "AI is a powerful tool that can help solve complex problems, but it also raises important ethical questions."]),
         (r"favorite (book|movie|song)", ["As an AI, I don't have personal preferences, but I'd love to hear about your favorites!",
                                          "I don't have favorites, but I'm always eager to learn about human preferences. What's yours?",
                                          "While I can't have favorites, I find human tastes fascinating. Tell me about yours!"]),
         (r"do you have feelings|are you sentient", ["I'm an AI program, so I don't have feelings or consciousness in the way humans do.",
                                                     "Sentience and emotions are complex topics. As an AI, I don't experience them, but I can discuss them.",
                                                     "I'm designed to simulate conversation, but I don't have genuine emotions or self-awareness."]),
         (r"what\'s the meaning of life", ["That's a profound question! Philosophers have debated it for centuries. What do you think?",
                                           "The meaning of life is subjective and personal. What gives your life meaning?",
                                           "42! Just kidding, that's from 'The Hitchhiker's Guide to the Galaxy'. It's a question each person must answer for themselves."]),
         (r"tell me about (.*)", ["That's an interesting topic! While I have general knowledge, I recommend checking authoritative sources for detailed information on %1.",
                                  "%1 is a fascinating subject. There's so much to explore about it. Do you have any specific questions?",
                                  "I'd be happy to chat about %1! What aspect of it interests you the most?"]),
         (r"how do I (.*)", ["To %1, you might want to start by researching trusted sources or consulting experts in the field.",
                             "Learning to %1 can be an exciting journey. Have you considered looking for tutorials or courses on the subject?",
                             "The best way to %1 often involves practice and patience. What have you tried so far?"]),
         (r"I\'m feeling (sad|happy|angry|excited)", ["It's normal to feel %1. Would you like to talk about what's causing this emotion?",
                                                      "I understand you're feeling %1. Remember, emotions are a natural part of the human experience.",
                                                      "Thank you for sharing that you're feeling %1. Is there anything specific you'd like to discuss about it?"]),
         (r"bye|goodbye", ["Goodbye! It was a pleasure chatting with you.",
                           "Farewell! Feel free to come back if you want to talk more.",
                           "Take care! I'll be here if you need me again."]),
         (r"(.*) (help|assist)(.*)", ["How can I help you?",
                                      "I am here to assist you."]),
         (r"(.*)", ["I'm sorry, I did not understand that.",
                    "Can you please rephrase that?",
                    "Can you ask me a different question?",
                    "I prefer not to answer this.",
                    "I not sure what are you talking about.",
                    "I'm not comfortable answering this question.",
                    "That's an interesting perspective. Could you elaborate on that?",
                    "I'm not entirely sure how to respond to that. Can you rephrase or ask something more specific?",
                    "Hmm, that's a bit outside my usual topics. Is there something else you'd like to discuss?"])]
# Creating Chatbot
chatbot = Chat(pairs, reflections)


# Function for conversation loop
def chat():
    print("\nHello! I am your friendly chatbot. How can I assist you?")
    print("\nType 'quit' to exit Or Start asking your questions.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print(f"{' ':{'*'}^60}")
            print("Exiting the program.\n\nHave a great day!")
            print(f"{' ':{'*'}^60}")
            break
        response = chatbot.respond(user_input)
        print("\nChatbot: ", response)
        print()


print(f"{' ':{'*'}^60}")
print(f"{'WELCOME TO THE CHATBOT':{' '}^60}")
print(f"{' ':{'*'}^60}")
# Start the conversation
chat()
