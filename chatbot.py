import sys
import time
from colorama import Fore, Style

class Chatbot:
    def __init__(self, ollama_api):
        self.ollama_api = ollama_api

    def simulate_typing(self, text, delay=0.009):
        """
        Function to simulate typing effect in console for a more interactive experience.
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def format_response(self, response):
        """
        Format response with colors for numbers and code snippets.
        """
        formatted_response = ""
        for char in response:
            if char.isdigit():
                formatted_response += Fore.BLUE + char + Style.RESET_ALL
            elif char == '`':
                formatted_response += Fore.GREEN + char + Style.RESET_ALL
            else:
                formatted_response += char
        return formatted_response

    def display_welcome_message(self):
        welcome_message = Fore.GREEN + "Chatbot: Hello! Type 'exit' to quit." + Style.RESET_ALL
        self.simulate_typing(welcome_message)

    def display_exit_message(self):
        exit_message = Fore.RED + "Chatbot: Goodbye! See you next time!" + Style.RESET_ALL
        self.simulate_typing(exit_message)

    def chat(self):
        """
        Start the chat loop.
        """
        self.display_welcome_message()
        while True:
            user_input = input("\n"+Fore.YELLOW + "You: " + Style.RESET_ALL)

            if user_input.lower() == "exit":
                self.display_exit_message()
                break

            response = self.ollama_api.chat_with_ollama(user_input)
            formatted_response = self.format_response(response)
            self.simulate_typing(Fore.CYAN + f"Chatbot: {formatted_response}" + Style.RESET_ALL)
