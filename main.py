from ollama_api import OllamaAPI
from chatbot import Chatbot

def main():
    ollama_api = OllamaAPI()  # Initialize Ollama API object
    chatbot = Chatbot(ollama_api)  # Initialize Chatbot object
    chatbot.chat()  # Start the chatbot

if __name__ == "__main__":
    main()
