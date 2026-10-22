def show_messages(text_messages):
    for message in text_messages:
        print(message)

def classify_message(text_messages, sent_messages):
    
    while text_messages:
        message = text_messages.pop(0)
        sent_messages.append(message)



text_messages = ["Je t'aime Andreina", "Tu es de loin la plus belle", "Je ne vais jamais t'abandonner"]
sent_messages = []

print("\nOriginal messages:")
classify_message(text_messages[:], sent_messages)

print("\nSent messages:")
show_messages(sent_messages)