import os
import google.generativeai as genai
from termcolor import colored, cprint

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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



def chat_with_gemini():
    print_gemini_cli_art()
    cprint("Chat with ✨ Gemini AI! Type 'exit' to end the conversation.", "magenta", "on_black")
    print("")
    
    conversation_history = []

    while True:
        cprint("You: ", "green", "on_black")
        user_input = input()
        print("")
        if user_input.lower() == 'exit':
            print("Ending chat. Goodbye!")
            break
        
        conversation_history.append({"role": "user", "parts": [{"text": user_input}]})
        
        chat_session.history = conversation_history  
        response = chat_session.send_message(user_input)
        
        conversation_history.append({"role": "model", "parts": [{"text": response.text}]})
        
        cprint(f"✨ Gemini: \n{response.text}", "magenta", "on_black")
        print("")

if __name__ == "__main__":
    chat_with_gemini()