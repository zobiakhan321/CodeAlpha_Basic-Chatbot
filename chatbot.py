# Simple Rule-Based Chatbot

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined responses
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm fine, thank you!",
        "what's your name": "I'm a simple chatbot created with Python.",
        "bye": "Goodbye! Have a great day!",
        "help": "You can try saying: hello, how are you, bye, or what's your name."
    }

    return responses.get(user_input, "I'm sorry, I don't understand that.")

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        response = get_bot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
