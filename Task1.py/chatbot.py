import re

# Define some sample responses
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a chatbot created by an AI. What's your name?",
    "bye": "Goodbye! Have a nice day!",
}

# Function to match user input with a predefined pattern
def match_pattern(input_text):
    for pattern, response in responses.items():
        if re.search(pattern, input_text, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that."

# Main function to run the chatbot
def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = match_pattern(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
