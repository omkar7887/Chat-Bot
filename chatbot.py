def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define predefined rules and responses
    greetings = ['hello', 'hi', 'hey']
    farewells = ['bye', 'goodbye', 'see you']
    questions = ['how are you', 'what is your name', 'who created you']

    # Check user input against predefined rules
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day."

    elif any(question in user_input for question in questions):
        if 'how are you' in user_input:
            return "I'm just a computer program, but I'm doing well. Thanks for asking!"
        elif 'what is your name' in user_input:
            return "Manu."
        elif 'who created you' in user_input:
            return "I was created by a programmer using Python."

    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask another question?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
