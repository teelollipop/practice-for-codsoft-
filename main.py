#Install the regex library for pattern recognition 
#Create a dictionary of user inputs and pattern response pairs
rules = {
    r'hello|hi|hey': 'Hello! How can I assist you?',
    r'bye|goodbye': 'Goodbye! Have an amazing day!',
    r'how are you': 'I am just a chatbot, but thanks for asking!',
    r'what is your name': 'My name is ChatTAI, an AI system created by Treasure Abaa',
    r'what can you do': 'I provide text based responses based on user inputs',
    r'help|?': 'I can provide basic information. Try asking a question.'
}

#Create chatbot response function
#Import the regular expresions module
import re

def chatbot_response(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I didn't understand that."

#Create a loop to take user input and provide responses until the user decides to exit
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
