#Create chatbot response function
#Import the regular expresions module

import re

def chatbot_response(user_input, rules):
    response = None
    for pattern in rules:
        pattern_with_wildcard = str(pattern) + '*'     
#Add '*' as a wildcard to the pattern
      
        if re.search(pattern_with_wildcard, user_input, re.IGNORECASE):
            response = rules[pattern]
            break
          
    if response is None:
      #Check if no match was found
      return "I'm sorry, I didn't understand that."
      
    return response 

#Define rules by creating a dictionary of user inputs and pattern response pairs

rules = {
    r'hello|hi|hey': 'Hello! How can I assist you?',
    r'bye|goodbye': 'Goodbye! Have an amazing day!',
    r'how are you': 'I am just a chatbot, but thanks for asking!',
    r'what is your name': 'My name is ChatTAI, an AI system created by Treasure Abaa',
    r'what can you do': 'I can provide text based responses based on user inputs',
    r'help|?': 'I can provide basic information. Try asking a question.', } 

#Create main loop for interacting with the chatbot 
#This loop takes user input and provide responses until the user decides to exit

while True:
    user_input = input("You: ")
    if user_input.strip() == '':
        print("Please enter a valid input.")
        continue

    response = chatbot_response(user_input, rules)
    print("Chatbot:", response)
