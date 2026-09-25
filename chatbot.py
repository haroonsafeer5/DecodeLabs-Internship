# ==========================================
# 1. EXPANDED KNOWLEDGE BASE (Dictionary)
# ==========================================
responses = {
    # Basic Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hey there! What can I do for you?",
    "hey": "Hey! How is your day going?",
    "good morning": "Good morning! Hope you have a productive day ahead.",
    "good evening": "Good evening! How can I assist you right now?",
    
    # Casual / Small Talk
    "how are you": "I am doing great, thank you for asking! How about you?",
    "what is your name": "I am a Rule-Based AI Chatbot built for DecodeLabs.",
    "who created you": "I was created as part of the DecodeLabs AI Internship program.",
    "what can you do": "I can answer questions, guide you about DecodeLabs, and process basic text queries!",
    "thank you": "You're very welcome! Let me know if you need anything else.",
    "thanks": "Anytime! Happy to help.",
    
    # Internship & Tech Info
    "decodelabs": "DecodeLabs is an awesome platform offering project-based learning and internships!",
    "python": "Python is a high-level, versatile programming language known for its simplicity and power in AI/ML.",
    "github": "GitHub is a cloud platform for version control and collaborating on code using Git.",
    "week 1": "Week 1 is all about building a Rule-Based AI Chatbot using basic Python logic!",
    
    # Help & Contact Options
    "help": "You can ask me about DecodeLabs, Python, Github, or general greetings!",
    "options": "Try typing: 'hello', 'decodelabs', 'python', 'github', 'week 1', or 'who created you'."
}

# Welcome Display
print("=" * 45)
print("   Welcome to DecodeLabs AI Chatbot 🤖   ")
print("=" * 45)
print("Note: Type 'exit', 'bye', or 'quit' to stop.")
print("Tip: Type 'help' or 'options' to see commands.\n")

# ==========================================
# 2. MAIN CONVERSATION LOOP
# ==========================================
while True:
    # User Input
    user_input = input("You: ")
    
    # Input Sanitization
    sanitized_input = user_input.lower().strip()
    
    # Handle empty press
    if not sanitized_input:
        continue

    # Exit Strategy
    if sanitized_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a fantastic day ahead. 🚀")
        break
    
    # Rule Matching & Fallback
    if sanitized_input in responses:
        print(f"Bot: {responses[sanitized_input]}")
    else:
        print("Bot: I'm sorry, I don't understand that question yet. Type 'options' to see what I know!")