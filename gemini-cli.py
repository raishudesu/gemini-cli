import os
from dotenv import load_dotenv
import google.generativeai as genai
from termcolor import colored, cprint
from rich.console import Console
from rich.markdown import Markdown


# Load the .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create the model with desired configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

console = Console()

def print_gemini_cli_art():
    art = r"""
  ____                   _       _ _     ____ _ _       
  ________  _______   _____ ______   ___  ________   ___          ________  ___       ___         
|\   ____\|\  ___ \ |\   _ \  _   \|\  \|\   ___  \|\  \        |\   ____\|\  \     |\  \        
\ \  \___|\ \   __/|\ \  \\\__\ \  \ \  \ \  \\ \  \ \  \       \ \  \___|\ \  \    \ \  \       
 \ \  \  __\ \  \_|/_\ \  \\|__| \  \ \  \ \  \\ \  \ \  \       \ \  \    \ \  \    \ \  \      
  \ \  \|\  \ \  \_|\ \ \  \    \ \  \ \  \ \  \\ \  \ \  \       \ \  \____\ \  \____\ \  \     
   \ \_______\ \_______\ \__\    \ \__\ \__\ \__\\ \__\ \__\       \ \_______\ \_______\ \__\    
    \|_______|\|_______|\|__|     \|__|\|__|\|__| \|__|\|__|        \|_______|\|_______|\|__|    
                                                                                                 
                                                                                                 
                                                                                                 
    """
    cprint(art, "magenta", "on_black")



def save_conversation_to_file(conversation_history):
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        for message in conversation_history:
            file.write(f"{message['role'].capitalize()}: {message['parts']}\n\n")
    print("Chat history saved to 'chat_history.txt'.")

def chat_with_gemini():
    print_gemini_cli_art()
    cprint("Chat with ✨ Gemini AI! \nType 'exit' to end the conversation.\nType 'export' to export and end the conversation.", "magenta", "on_black")
    print("")
    
    conversation_history = []

    while True:
        user_input = input(colored("You: \n", "green"))
        print("")
        if user_input.lower() == 'exit':
            print("Ending chat. Goodbye!")
            break

        if user_input.lower() == 'export':
            save_conversation_to_file(conversation_history)
            print("Ending chat. Conversation saved in chat_history.txt file. Goodbye!")
            break
        
        conversation_history.append({"role": "user", "parts": [{"text": user_input}]})
        
        chat_session.history = conversation_history  
        response = chat_session.send_message(user_input)
        
        conversation_history.append({"role": "model", "parts": [{"text": response.text}]})

        parsed_response = Markdown(response.text)
        
        cprint(f"----------------------------------------\n", "magenta")
        cprint(f"✨ Gemini: \n", "magenta")
        console.print(parsed_response)
        cprint(f"----------------------------------------\n", "magenta")
        print("")

if __name__ == "__main__":
    chat_with_gemini()