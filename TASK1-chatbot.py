
print("Hello! I'm a simple chatbot. You can ask me things (type 'exit' to stop).")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print("Bot: Hello! How can I help you?")
    elif "your name" in user_input:
        print("Bot: I'm just a Python chatbot, no fancy name yet!")
    elif "help" in user_input:
        print("Bot: You can ask me basic questions, and I'll try to answer.")
    elif "python" in user_input:
        print("Bot: Python is a powerful and beginner-friendly programming language.")
    elif "bye" in user_input or user_input == "exit":
        print("Bot: See you later. Take care!")
        break
    else:
        print("Bot: Hmm, I didn't understand that. Try something else.")
