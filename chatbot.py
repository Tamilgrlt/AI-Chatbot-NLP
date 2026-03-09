import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
import random
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

knowledge_base = {
"hello":"Hello! How can I help you?",
"hi":"Hi there!",
"good morning":"Good morning!",
"good evening":"Good evening!",
"how are you":"I am fine. How can I assist you?",
"what is your name":"I am an AI chatbot.",
"who created you":"I was created using Python and NLP.",
"what is python":"Python is a programming language.",
"what is ai":"AI stands for Artificial Intelligence.",
"what is machine learning":"Machine learning is a subset of AI.",
"what is deep learning":"Deep learning uses neural networks.",
"what is nlp":"Natural Language Processing.",
"what is chatbot":"A chatbot is a program that talks with users.",
"what is computer":"An electronic machine.",
"what is internet":"A global network.",
"what is programming":"Writing instructions for computers.",
"what is software":"Programs running on computer.",
"what is hardware":"Physical components of computer.",
"what is cloud computing":"Internet-based computing.",
"what is database":"System to store data.",
"what is sql":"Structured Query Language.",
"what is html":"Language used to create web pages.",
"what is css":"Used to style web pages.",
"what is javascript":"Web scripting language.",
"what is java":"Popular programming language.",
"what is linux":"Open source operating system.",
"what is windows":"Operating system developed by Microsoft.",
"what is github":"Code hosting platform.",
"what is algorithm":"Step-by-step problem solving.",
"what is data structure":"Organizing data efficiently.",
"what is loop":"Repeating instructions.",
"what is function":"Reusable block of code.",
"what is variable":"Storage location for data.",
"what is list":"Collection of items.",
"what is dictionary":"Key-value data structure.",
"what is tuple":"Immutable list.",
"what is class":"Blueprint of objects.",
"what is object":"Instance of class.",
"what is api":"Application Programming Interface.",
"what is json":"Data format used for APIs.",
"what is xml":"Markup language for data.",
"what is cybersecurity":"Protecting computer systems.",
"what is encryption":"Securing data.",
"what is google":"Popular search engine.",
"what is facebook":"Social media platform.",
"what is instagram":"Photo sharing platform.",
"what is twitter":"Social media platform.",
"what is youtube":"Video sharing platform.",
"what is amazon":"E-commerce company.",
"what is microsoft":"Technology company.",
"what is apple":"Technology company.",
"what is tesla":"Electric vehicle company.",
"what is blockchain":"Technology behind cryptocurrency.",
"what is bitcoin":"Digital currency.",
"what is ethereum":"Cryptocurrency platform.",
"what is metaverse":"Virtual digital world.",
"what is virtual reality":"Immersive digital environment.",
"what is augmented reality":"Digital objects in real world.",
"what is iot":"Internet of Things.",
"what is big data":"Large data analysis.",
"what is data mining":"Finding patterns in data.",
"what is neural network":"AI model inspired by brain.",
"what is chatbot used for":"Customer support and automation.",
"what is automation":"Using technology to perform tasks.",
"what is robotics":"Designing robots.",
"what is python used for":"AI, web development, data science.",
"what is flask":"Python web framework.",
"what is django":"Python web framework.",
"what is tensorflow":"Machine learning library.",
"what is pytorch":"Deep learning framework.",
"what is numpy":"Python numerical library.",
"what is pandas":"Data analysis library.",
"what is matplotlib":"Data visualization library.",
"what is seaborn":"Statistical visualization library.",
"what is jupyter notebook":"Interactive coding environment.",
"what is vs code":"Code editor.",
"what is compiler":"Converts code to machine language.",
"what is interpreter":"Executes code line by line.",
"what is operating system":"Manages computer resources.",
"what is android":"Mobile operating system.",
"what is ios":"Apple mobile OS.",
"what is wifi":"Wireless internet connection.",
"what is bluetooth":"Wireless communication technology.",
"what is firewall":"Network security system.",
"what is antivirus":"Software to remove viruses.",
"what is malware":"Malicious software.",
"what is phishing":"Cyber attack using fake messages.",
"what is password":"Security key for accounts.",
"what is username":"User identity.",
"what is login":"Accessing an account.",
"what is logout":"Exiting an account.",
"what is chatbot example":"Siri, Alexa, Google Assistant.",
"what is siri":"Apple voice assistant.",
"what is alexa":"Amazon voice assistant.",
"what is google assistant":"Google voice assistant.",
"bye":"Goodbye! Have a nice day!"
}

def preprocess(text):
    text=text.lower()
    tokens=word_tokenize(text)
    tokens=[lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def chatbot_response(user_input):
    processed=preprocess(user_input)

    for key in knowledge_base:
        if key in processed:
            return knowledge_base[key]

    return "Sorry, I don't understand."

print("AI Chatbot using NLP (type 'bye' to exit)\n")

while True:
    user_input=input("You: ")

    if user_input.lower()=="bye":
        print("Bot: Goodbye!")
        break

    response=chatbot_response(user_input)
    print("Bot:",response)