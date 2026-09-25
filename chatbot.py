# 1. Knowledge Base (Dictionary with 5+ intents)
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hey there! What can I do for you?",
    "how are you": "I am doing great, thank you for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot built for DecodeLabs.",
    "what can you do": "I can respond to basic queries using deterministic rule matching!",
    "who created you": "I was created as part of the DecodeLabs AI Internship program."
}

print("--- Welcome to DecodeLabs AI Chatbot ---")
print("Type 'exit', 'bye', or 'quit' to end the conversation.\n")

# 2. Input Loop (Continuous while cycle)
while True:
    # Get user input
    user_input = input("You: ")
    
    # 3. Sanitization (Lowercase and Whitespace removal)
    sanitized_input = user_input.lower().strip()
    
    # 4. Exit Strategy
    if sanitized_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a great day ahead. 🚀")
        break
    
    # Check if input is empty
    if not sanitized_input:
        continue

    # 5. Rule Matching & Fallback Handling
    # Fast O(1) Dictionary Lookup
    if sanitized_input in responses:
        print(f"Bot: {responses[sanitized_input]}")
    else:
        # Fallback response for unknown queries
        print("Bot: I'm sorry, I don't understand that question yet. Can you ask something else?")