import datetime
import time

name =input("Enter your name: ")
currentHour = datetime.datetime.now().hour
if 5 <= currentHour <= 11:
    print(f"Good morning {name}!")
elif 11 <= currentHour <= 17:
    print(f"Good afternoon {name}!")
elif 17 <= currentHour <= 20:
    print(f"Good evening {name}")
else:
    print(f"Good night {name}")


#intro
print("Welcome to Rule based chatbot!!")
print("You can talk to me and I will try to answer your questions.Type 'bye' to exit from the chatbot.")

#chatbot memory: dictionary of responses
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm doing well, thank you! How about you?",
    "what is your name": "I am a Rule based chatbot. I don't have a name, but you can call me Chatbot!",
    "who are you":"I am a Rule based chatbot. I am here to help you with your questions and have a conversation with you.",
    "motivate me": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "tell me about python": "Python is a high-level programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, and more.",
    "bye": "Goodbye! Have a great day!"
}

#function to get response of chatbot
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    
    return "I am still in learning mode. Cannot answer this question!"

#take user input
while True:
    userInput= input("How can i help you: ")
    reply = getResponseBot(userInput)
    print("Bot response: ",reply)

    if "bye" in userInput.lower():
        break
       
        
    