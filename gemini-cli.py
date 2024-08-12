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

# Create the Gemini Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Instantiate the Console from Rich package to parse Gemini responses
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


# Export conversation as .txt file in Desktop directory
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "chat_history.txt")

def save_conversation_to_file(conversation_history):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for message in conversation_history:
                file.write(f"{message['role'].capitalize()}: {message['parts']}\n\n")
        print("Chat history saved to your Desktop directory as 'chat_history.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred while exporting the conversation history: {e}")

def chat_with_gemini():
    print_gemini_cli_art()
    cprint("Chat with ✨ Gemini AI! \nType 'exit' to end the conversation.\nType 'export' to export and end the conversation.\n", "magenta", "on_black")
    cprint("Made by raishudesu on Github", "magenta", "on_black")
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

        try: 
            # Add the user prompt to conversation history
            conversation_history.append({"role": "user", "parts": [{"text": user_input}]})
            
            # Update chat session history
            chat_session.history = conversation_history  
            
            # Send message to the model to get response
            response = chat_session.send_message(user_input)
            
            # Add the model response to conversation history
            conversation_history.append({"role": "model", "parts": [{"text": response.text}]})

            # Parse model response (in Markdown format)
            parsed_response = Markdown(response.text)
            
            cprint(f"----------------------------------------\n", "magenta")
            cprint(f"✨ Gemini: \n", "magenta")
            console.print(parsed_response)
            cprint(f"----------------------------------------\n", "magenta")
            print("")

        except Exception as e:
            cprint(f"An unexpected error occurred: {e}", "red", "on_black")
            

if __name__ == "__main__":
    chat_with_gemini()


# DEV NOTES
# Add feature to select a conversation history to restore/access/continue conversation with Gemini if exist
# Make this Gemini CLI as a package and can be called anytime in terminals 